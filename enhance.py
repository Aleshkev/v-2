import functools
import logging
import re
import traceback
from pathlib import Path
from typing import *

import bs4
import hyphen
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileModifiedEvent
from watchdog.observers import Observer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

assert __name__ == "__main__"


@functools.lru_cache(32)
def _get_hyphenator(lang: str):
    lang = {"en": "en_GB", "pl-pl": "pl_PL"}.get(lang, f"{lang}_{lang.upper()}")
    log.info(f"Creating Hyphenator for {lang}")
    return hyphen.Hyphenator(lang)


def _hyphenate(s: str, lang: str):
    if re.match(r"\$.*\$", s):
        return s
    was_upper = s.isupper()
    if was_upper:
        s = s.lower()  # Because the hyphenator doesn't like all-uppercase strings.

    syllables = _get_hyphenator(lang).syllables(s)
    s = "\xad".join(syllables) if syllables else s
    return s.upper() if was_upper else s


@functools.lru_cache(1)
def _get_language_identifier():
    log.info(f"Creating LanguageIdentifier")
    import langid
    identifier = langid.langid.LanguageIdentifier.from_modelstring(langid.langid.model, norm_probs=True)
    identifier.set_languages(["en", "pl", "fr", "de", "ru"])
    return identifier


def _walk_strings(node, lang=None):
    if isinstance(node, bs4.NavigableString):
        yield node, lang
        return
    if isinstance(node, bs4.Comment) or node.name in {"code", "style", "script"}:
        return
    for child in node.children:
        yield from _walk_strings(child, lang if "lang" not in node.attrs.keys() else node.attrs["lang"])


def walk_strings(soup) -> Iterator[Tuple[bs4.NavigableString, str]]:
    yield from _walk_strings(soup.find("body"), lang=soup.find("html").get("lang", "pl"))


def detect_lang(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        text = str(node)
        if re.search(r"\w", text) and len(tuple(node.parent.children)) == 1 and not node.parent.lang:
            another_lang, probability = _get_language_identifier().classify(text)
            if probability > 0.9 and another_lang != lang:
                node.parent.attrs["lang"] = another_lang


def insert_soft_hyphens(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        s = re.sub(r"(\$\S.*?\S\$|\w+)", lambda m: _hyphenate(m.group(0), lang), node.string)
        node.string.replace_with(s)


def prevent_orphans(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        s = re.sub(r"(([^\w]|^)\w)(\s|^)", r"\1" + "\xa0", node.string)
        # This is an ugly hack, but better than 'correcting' the regex above.
        s = re.sub(r"(([^\w]|^)\w)\s(\w)(\s|^)", r"\1" + "\xa0" + r"\3" + "\xa0", s)
        node.string.replace_with(s)


def readjust_dialog_spacing(soup):
    for node, lang in walk_strings(soup):
        node.string.replace_with(re.sub(r"(^\s*—)\s", r"\1 ", node.string))


def change_quotes(soup):
    for node, lang in walk_strings(soup):
        if lang == "pl":
            s = re.sub(r"“", "„", node.string)
            s = re.sub(r"”", "”", s)
            node.string.replace_with(s)


def process(p: Path, continuous: bool = False):
    if p.suffix != ".html":
        return
    heart = "<!-- ❤ -->"
    with p.open(encoding="utf-8") as f:
        if continuous and heart in f.readline():
            return
    try:
        s = p.read_text("utf-8")
        log.info(f"Processing {p}")
        soup = bs4.BeautifulSoup(s, "html.parser")
        detect_lang(soup)
        insert_soft_hyphens(soup)
        prevent_orphans(soup)
        readjust_dialog_spacing(soup)
        change_quotes(soup)
        p.write_text((heart + "\n" if continuous else "") + str(soup), "utf-8")
    except:
        traceback.print_exc()
        raise


f = Path(Path(__file__).parent / "public")

for p in f.glob("**/*.html"):
    process(p)


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not isinstance(event, (FileCreatedEvent, FileModifiedEvent)):
            return
        p = Path(event.src_path)
        process(p)


observer = Observer()
# observer.schedule(Handler(), str(f), recursive=True)
# observer.start()
#
# try:
#     while True:
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     observer.stop()
# observer.join()
