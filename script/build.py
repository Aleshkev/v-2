import argparse
import dataclasses
import datetime
import itertools
import logging
import os
import pathlib
import re
import shutil
import subprocess
from typing import *

import htmlmin
import jinja2
import slugify
import webassets.ext.jinja2
import yaml

import functional_transforms
import typographical_transforms

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

HTML = NewType('HTML', str)


@dataclasses.dataclass
class Article:
    source: pathlib.Path
    date: Optional[datetime.date] = None
    revised: Optional[datetime.date] = None
    extra_copyright: Optional[HTML] = ""  # See "Paski TVP" for example.
    title: HTML = ""
    content: HTML = ""

    def __repr__(self):
        return f"<{self.title.replace('­', '')}>"


class Site:
    def __init__(self, expensive_typography: bool, clear_output: bool, article_filter: Optional[str],
                 release: bool, minimal: bool):
        self.expensive_typography = expensive_typography
        self.article_filter = article_filter
        self.release = release
        self.minimal = minimal

        self.source_dir = pathlib.Path("content/")
        self.output_dir = pathlib.Path("a/")
        self.script_dir = pathlib.Path(__file__).parent
        self.theme_dir = pathlib.Path("theme/")
        self.release_root = "https://aleshkev.github.io/"
        self.root = self.release_root if self.release else "/aleshkev.github.io/"

        self.articles = []

        self.environment = jinja2.Environment(
            loader=jinja2.PackageLoader(__name__, os.path.relpath(self.theme_dir, self.script_dir)),
            extensions=[webassets.ext.jinja2.AssetsExtension],
            autoescape=False)
        self.environment.filters["as_absolute_url"] = self.as_absolute_url
        self.environment.assets_environment = webassets.Environment(
            str(self.output_dir), self.root + str(self.output_dir),
            load_path=[str(self.theme_dir)])
        self.environment.assets_environment.url_expire = False
        self.environment.assets_environment.debug = not self.release
        self.article_template = self.environment.get_template("article.html")
        self.index_template = self.environment.get_template("index.html")

        self.resources: Dict[pathlib.Path, pathlib.Path] = {}
        for directory, subdirectories, files in os.walk(self.source_dir):
            for file in files:
                self.add_resource(pathlib.Path(directory) / file)

        if clear_output and self.output_dir.is_dir():
            shutil.rmtree(self.output_dir)

        self.load_articles()
        for article in self.articles:
            log.info(f"Load {article.source}")
            self.load_article_data(article)

        self.index = self.source_dir / "index"
        self.add_resource(self.index, virtual=True)

        self.articles.sort(key=lambda article: article.date, reverse=True)

        for article in self.articles:
            self.render_article(article)

        self.render_index()

    def add_resource(self, source_file: pathlib.Path, virtual: bool = False):
        o = source_file
        if source_file.suffix == ".md" or virtual:
            o = (self.output_dir / os.path.relpath(str(source_file), self.source_dir)).with_suffix(".html")
        self.resources[source_file] = o
        os.makedirs(o.parent, exist_ok=True)

    def as_absolute_url(self, source_file: pathlib.Path, force_release: bool = False):
        p = self.resources[source_file]
        if p.name == "index.html":
            p = p.parent
        if (force_release or self.release) and p.suffix == ".html":
            p = p.with_suffix("")

        return (self.release_root if force_release else  self.root) + str(p).replace("\\", "/")

    def load_articles(self):
        for file in self.resources.keys():
            if file.suffix != ".md":
                continue
            if self.article_filter and self.article_filter not in file.name:
                continue
            if file.name.endswith("-draft" + file.suffix) and self.minimal:
                continue

            match = re.fullmatch(r"([0-9]{4})-([0-9]{2})-([0-9]{2})-(.*)\.md", file.name)
            if match:
                *date, slug = match.groups()
                date = datetime.date(*map(int, date))
            else:
                date = datetime.date.today()

            self.articles.append(Article(file, date=date))

    @staticmethod
    def extract_metadata(md_source: str) -> Tuple[Dict[str, Any], str]:
        metadata_match = re.fullmatch(r"---\n(.*?)---\n(.*)", md_source, re.DOTALL)
        if metadata_match:
            return yaml.safe_load(metadata_match.group(1)), metadata_match.group(2)
        return {}, md_source

    def load_article_data(self, article):
        md_source = article.source.read_text("utf-8")
        metadata, md_source = self.extract_metadata(md_source)

        article.revised = metadata.get("revised", None)
        assert article.revised is None or isinstance(article.revised, datetime.date)

        article.extra_copyright = metadata.get("extra-copyright", None)

        p = subprocess.run(['node', str(self.script_dir / 'markdown.js')],
                           input=md_source.encode("utf-8"), capture_output=True)
        assert not p.stderr, p.stderr.decode("utf-8")

        soup = functional_transforms.get_soup(p.stdout.decode("utf-8"))
        article.title = functional_transforms.extract_title(soup)
        article.content = str(soup)

    def render_something(self, source: pathlib.Path, template: jinja2.Template, data: Dict[str, Any]):
        log.info(f"Render {source}")
        output_file = self.resources[source]
        soup = functional_transforms.get_soup(template.render(**data, site=self))
        functional_transforms.resolve_hrefs(soup, source, self.as_absolute_url)
        functional_transforms.handle_images(soup)
        if self.expensive_typography:
            typographical_transforms.detect_lang(soup)
        typographical_transforms.insert_nbsp(soup)
        typographical_transforms.insert_shy(soup)
        typographical_transforms.extend_emphases(soup)
        s = str(soup)
        # if self.release:
        #     s = htmlmin.minify(s)
        output_file.write_text(s, "utf-8")

    def render_article(self, article: Article):
        self.render_something(article.source, self.article_template, dict(article=article))

    def render_index(self):
        self.render_something(self.index, self.index_template, dict())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the site. Use -recm for release mode.")
    parser.add_argument("--expensive", "-e", action="store_true", help="waste time for nicer output")
    parser.add_argument("--clear", "-c", action="store_true", help="remove last build")
    parser.add_argument("--only", "-l", help="build only articles with paths containing this text")
    parser.add_argument("--release", "-r", action="store_true", help="final build to upload online")
    parser.add_argument("--minimal", "-m", action="store_true", help="skip unfinished articles")

    args = parser.parse_args()
    Site(args.expensive, args.clear, args.only, args.release, args.minimal)
