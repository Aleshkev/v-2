from typing import *
import pathlib
import shutil
import logging

import CommonMark
import htmlmin
import jinja2
import webassets.ext.jinja2

from . import transforms


def render(content: pathlib.Path, theme: pathlib.Path, root_url: str,
           output: pathlib.Path, html_extensions: bool = True):
    assert root_url.endswith('/')

    content = content.absolute().resolve()
    theme = theme.absolute().resolve()
    output = output.absolute().resolve()

    logging.info(f"Rendering {content}")
    logging.info(f"theme:    {theme}")
    logging.info(f"root_url: {root_url}")
    logging.info(f"output:   {output}")

    templates = jinja2.Environment(loader=jinja2.FileSystemLoader([theme]),
                                   extensions=[webassets.ext.jinja2.AssetsExtension])
    templates.assets_environment = webassets.Environment(output, root_url, load_path=[theme])
    every = templates.get_template('every.html')

    parser = CommonMark.Parser()
    renderer = CommonMark.HtmlRenderer()

    logging.info("Loading and rendering [nav]")
    nav_ast = parser.parse((content / 'nav.md').read_text('utf-8'))
    transforms.resolve_links(nav_ast, root_url, keep_extension=html_extensions)
    nav = renderer.render(nav_ast)

    logging.info("Loading and rendering [footer]")
    footer_ast = parser.parse((content / 'footer.md').read_text('utf-8'))
    transforms.resolve_links(footer_ast, root_url, keep_extension=html_extensions)
    footer = renderer.render(footer_ast)

    logging.info("Loading [site-name]")
    site_name = (content / 'site-name.txt').read_text('utf-8').strip()

    exclude = ('nav.md', 'footer.md', 'site-name.txt')

    # TODO: Handle not-flat structure of markdown files.
    for md_file in content.glob('*.md'):
        if md_file.name in exclude:
            continue

        logging.info(f"Rendering {md_file}")
        ast = parser.parse(md_file.read_text('utf-8'))

        title = transforms.get_title(ast)
        title = title + ' -- ' + site_name if title is not None else site_name

        transforms.anchor_headings(ast)
        transforms.resolve_links(ast, root_url + md_file.stem + '.html', keep_extension=html_extensions)

        out = content / output / (md_file.stem + '.html')

        out_html = every.render(root_url=root_url, title=title, content=renderer.render(ast), nav=nav, footer=footer)
        out_html_min = htmlmin.minify(out_html)

        out.write_text(out_html_min, 'utf-8')

    for file in content.glob('*'):
        if file.suffix == '.md' or file.name in exclude:
            continue
        logging.info(f"Copying {file}")
        shutil.copy(str(file), str(output / file.name))
