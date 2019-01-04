from typing import *
import pathlib
import shutil
import logging

import commonmark
import htmlmin
import jinja2
import webassets.ext.jinja2

from . import transforms


logger = logging.getLogger(__name__)


def render(content: pathlib.Path, theme: pathlib.Path, root_url: str,
           output: pathlib.Path, html_extensions: bool = True):
    assert root_url.endswith('/')

    content = content.absolute().resolve()
    theme = theme.absolute().resolve()
    output = output.absolute().resolve()

    logger.info(f"Rendering Markdown from: {content}")
    logger.info(f"theme:    {theme}")
    logger.info(f"root_url: {root_url}")
    logger.info(f"output:   {output}")

    templates = jinja2.Environment(loader=jinja2.FileSystemLoader([theme]),
                                   extensions=[webassets.ext.jinja2.AssetsExtension])
    templates.assets_environment = webassets.Environment(output, root_url, load_path=[theme])
    every = templates.get_template('every.html')

    parser = commonmark.Parser()
    renderer = commonmark.HtmlRenderer()

    logger.info("Loading and rendering [nav]")
    nav_ast = parser.parse((content / 'nav.md').read_text('utf-8'))
    transforms.resolve_links(nav_ast, root_url, keep_extension=html_extensions)
    nav = renderer.render(nav_ast)

    logger.info("Loading and rendering [footer]")
    footer_ast = parser.parse((content / 'footer.md').read_text('utf-8'))
    transforms.resolve_links(footer_ast, root_url, keep_extension=html_extensions)
    footer = renderer.render(footer_ast)

    logger.info("Loading [site-name]")
    site_name = (content / 'site-name.txt').read_text('utf-8').strip()

    # TODO: Handle not-flat structure of markdown files.
    for md_file in content.glob('*.md'):
        if md_file.name in ('nav.md', 'footer.md', 'site-name.txt'):
            continue

        logger.info(f"Rendering {md_file}")
        ast = parser.parse(md_file.read_text('utf-8'))

        title = transforms.get_title(ast)
        title = title + ' -- ' + site_name if title is not None else site_name

        transforms.anchor_headings(ast)
        transforms.resolve_links(ast, root_url + md_file.stem + '.html', keep_extension=html_extensions)

        out = content / output / (md_file.stem + '.html')

        out_html = every.render(root_url=root_url, title=title, content=renderer.render(ast), nav=nav, footer=footer)

        out.write_text(out_html, 'utf-8')

