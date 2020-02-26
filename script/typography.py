import functools
import logging
import regex
import re
from typing import *

import bs4
import hyphen

log = logging.getLogger(__name__)


@functools.lru_cache(32)
def _get_hyphenator(lang: str):
    lang = "en_GB" if lang == "en" else f"{lang}_{lang.upper()}"
    print(lang)
    return hyphen.Hyphenator(lang)


def _hyphenate(s: str, lang: str):
    was_upper = s.isupper()
    if was_upper:
        s = s.lower()  # Because the hyphenator doesn't like all-uppercase strings.

    syllables = _get_hyphenator(lang).syllables(s)
    s = "\xad".join(syllables) if syllables else s
    return s.upper() if was_upper else s


@functools.lru_cache(1)
def _get_language_identifier():
    import langid
    log.info("Load language identifier")
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
    yield from _walk_strings(soup.find("body"), lang=soup.find("html").attrs["lang"])


def detect_lang(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        text = str(node)
        if re.search(r"\w", text) and len(tuple(node.parent.children)) == 1 and not node.parent.lang:
            another_lang, probability = _get_language_identifier().classify(text)
            if probability > 0.8 and another_lang != lang:
                node.parent.attrs["lang"] = another_lang


def insert_soft_hyphens(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        s = re.sub(r"\w+", lambda m: _hyphenate(m.group(0), lang), node.string)
        node.string.replace_with(s)


def prevent_orphans(soup: bs4.Tag):
    for node, lang in walk_strings(soup):
        s = re.sub(r"(([^\w]|^)\w)(\s|^)", r"\1" + "\xa0", node.string)
        # This is an ugly hack, but better than 'correcting' the regex above.
        s = re.sub(r"(([^\w]|^)\w)\s(\w)(\s|^)", r"\1" + "\xa0" + r"\3" + "\xa0", s)
        node.string.replace_with(s)


def _find_border_string(tag, index) -> Optional[bs4.NavigableString]:
    if tag is None:
        return None
    while not isinstance(tag, bs4.NavigableString):
        p = tuple(tag.children)
        if not p:
            return None
        tag = p[index]
    return tag


def readjust_dialog_spacing(soup):
    for node, lang in walk_strings(soup):
        node.string.replace_with(re.sub(r"(^\s*—)\s", r"\1 ", node.string))
