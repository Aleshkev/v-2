import functools
import logging
import regex
import re
from typing import *

import bs4
import hyphen

log = logging.getLogger(__name__)


@functools.lru_cache(20)
def _get_hyphenator(lang):
    if lang == "en":
        lang = "en_GB"
    else:
        lang += "_" + lang.upper()
    return hyphen.Hyphenator(lang)


def hyphenate(s: str, lang):
    was_upper = False
    if s.isupper():
        was_upper = True
        s = s.lower()

    # if s[0].isupper():
    #     return s

    syllables = _get_hyphenator(lang).syllables(s)
    if syllables:
        s = "\xad".join(syllables)

    if was_upper:
        s = s.upper()

    return s


@functools.lru_cache(1)
def _get_language_identifier():
    import langid
    log.info("Load language identifier")
    identifier = langid.langid.LanguageIdentifier.from_modelstring(langid.langid.model, norm_probs=True)
    identifier.set_languages(["en", "pl", "fr", "de", "ru"])
    return identifier


def _walk_strings(node, lang=None, ignore_headings=False):
    if isinstance(node, bs4.element.Comment):
        return
    if isinstance(node, bs4.element.NavigableString):
        yield node, lang
        return
    if node.name in ("code", "style", "script") or (
            ignore_headings and node.name in ("h1", "h2", "h3", "h4", "h5", "h6")):
        return
    for child in node.children:
        yield from _walk_strings(child, lang if "lang" not in node.attrs.keys() else node.attrs["lang"],
                                 ignore_headings)


def walk_strings(soup, ignore_headings=False) -> Iterator[Tuple[bs4.element.NavigableString, str]]:
    yield from _walk_strings(soup.find("body"), lang=soup.find("html").attrs["lang"], ignore_headings=ignore_headings)


# "<em>lingua franca</em>" → '<em lang="fr">lingua franca</em>'
# (Doesn't work very well.)
def detect_lang(soup: bs4.element.Tag):
    for node, lang in walk_strings(soup):
        text = str(node)
        if re.search(r"\w", text) and len(tuple(node.parent.children)) == 1 and not node.parent.lang:
            another_lang, probability = _get_language_identifier().classify(text)
            if probability > 0.8 and another_lang != lang:
                node.parent.attrs["lang"] = another_lang


# "disestablishment" → "dis&shy;es&shy;tab&shy;lish&shy;ment"
def insert_shy(soup: bs4.element.Tag):
    for node, lang in walk_strings(soup, ignore_headings=True):
        s = re.sub(r"\w+", lambda m: hyphenate(m.group(0), lang), node.string)
        node.string.replace_with(s)


# "i tak" → "i&nbsp;tak"
# "i z tym" → "i&nbsp;z&nbsp;tym"
def insert_nbsp(soup: bs4.element.Tag):
    for node, lang in walk_strings(soup):
        s = re.sub(r"(([^\w]|^)\w)(\s|^)", r"\1" + "\xa0", node.string)
        # This is an ugly hack, but better than 'correcting' the regex above.
        s = re.sub(r"(([^\w]|^)\w)\s(\w)(\s|^)", r"\1" + "\xa0" + r"\3" + "\xa0", s)
        node.string.replace_with(s)


def _find_border_string(tag, index) -> Optional[bs4.element.NavigableString]:
    if tag is None:
        return None
    while not isinstance(tag, bs4.element.NavigableString):
        p = tuple(tag.children)
        if not p:
            return None
        tag = p[index]
    return tag


# "A (<em>very</em>) sad <strong>occasion</strong>." → "A <em>(very)</em> sad <strong>occasion.</strong>"
def extend_emphases(soup, _elements=("em", "strong")):
    for node, lang in walk_strings(soup):
        s = node.string

        if node.previous_sibling and node.previous_sibling.name in _elements:
            m = regex.match(r"^\p{P}+", s)
            p = _find_border_string(node.previous_sibling, -1)
            if m and p:
                z, s = s[:m.end(0)], s[m.end(0):]
                p.string.replace_with(str(p) + z)

        if node.next_sibling and node.next_sibling.name in _elements:
            m = regex.match(r"\p{P}+$", s)
            p = _find_border_string(node.next_sibling, 0)
            if m and p:
                z, s = s[m.start(0):], s[:m.start(0)]
                p.string.replace_with(z + str(p))

        node.string.replace_with(s)


# "&emdash; Hi!" → "&emdash;&4emsp;Hi!", where &4emsp; is FOUR-PER-EM space.
# It looks like normal space, but hyphen-style dialogs look nicer when text-align is justified:
#   -- Hi! How are you?
#   -- Well.  And  you?
# instead of:
#   -- Hi! How are you?
#   --  Well.  And  you?
def improve_dialogs(soup):
    for node, lang in walk_strings(soup):
        node.string.replace_with(re.sub(r"(^\s*—)\s", r"\1 ", node.string))
