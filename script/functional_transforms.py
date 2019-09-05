import logging
import pathlib
import re

import bs4

log = logging.getLogger(__name__)


def get_soup(html):
    return bs4.BeautifulSoup(html, "html.parser")


def extract_title(soup: bs4.element.Tag):
    title: bs4.Tag = soup.find("h1")
    assert title
    s = "".join(map(str, title.children))
    title.decompose()
    return s


def hoist_footnotes(soup: bs4.element.Tag):
    e = soup.find("hr", class_="footnotes-sep")
    if not e:
        return
    e.decompose()
    footnotes = soup.find("section", class_="footnotes")
    if not footnotes:
        return
    for span in soup.find_all("span", class_="fn-anchor"):
        ref_id = span["data-id"]

        aside = footnotes.find("li", id=f"fn{ref_id}")
        aside.name = "aside"
        aside.find("a", class_="footnote-backref").decompose()
        span.attrs = aside.attrs = {"data-id": ref_id}
        span.append(bs4.NavigableString("\u200b"))  # Zero-width space, to be sure span has correct text height.

        parent: bs4.Tag = span.find_parent(
            lambda x: x.name in ("p", "ol", "ul", "blockquote", "table", "h1", "h2", "h3", "h4", "h5",
                                 "h6", "details"))
        append_to = parent.next_sibling
        while isinstance(append_to, bs4.NavigableString) and not append_to.strip():
            append_to = append_to.next_sibling
        if not append_to or append_to.get("class", "") != "asides":
            append_to = bs4.Tag(name="div")
            append_to["class"] = "asides"
            parent.insert_after(append_to)
        append_to.append(aside)
    footnotes.decompose()


def resolve_hrefs(soup: bs4.element.Tag, source: pathlib.Path, as_absolute_url):
    for node in soup.find("body").find_all(lambda tag: "href" in tag.attrs.keys()):
        s = node.attrs["href"]
        if re.match(r"^\w+://", s) or re.match(r"^/", s):
            continue
        try:
            s = as_absolute_url(source.parent / s)
            node.attrs["href"] = s
        except KeyError:
            log.warning(f"Broken inside-href: {s} not a resource")
