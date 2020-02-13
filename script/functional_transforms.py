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


def handle_images(soup: bs4.element.Tag):
    for p in soup.find_all("p"):
        p: bs4.element.Tag
        children = tuple(p.children)
        if len(children) != 1 or children[0].name != "img":
            continue
        img, = children

        img.extract()
        figure = bs4.element.Tag(name="figure")
        figure.insert(0, img)
        if img.attrs["alt"]:
            figcaption = bs4.element.Tag(name="figcaption")
            figcaption.string = bs4.element.NavigableString(img.attrs["alt"])
            figure.insert(1, figcaption)
        p.insert_after(figure)
        p.decompose()
