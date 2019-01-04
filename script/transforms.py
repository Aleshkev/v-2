from typing import *
import re
import urllib.parse

import commonmark, commonmark.node
import slugify


def print_ast(document: commonmark.node.Node):
    indent = 0
    for node, entering in document.walker():
        if entering:
            attrs = []
            for k in ('destination', 'title', 'info', 'level', 'list_data'):
                attr = getattr(node, k)
                if attr is not None and attr != {}:
                    attrs.append(f"{k}={attr!r}")
            print("  " * indent + str(node), "; ".join(attrs))

        if node.is_container():
            indent += 1 if entering else -1


def anchor_headings(document: commonmark.node.Node):
    in_heading = False
    chunks = []
    for node, entering in document.walker():
        node: commonmark.node.Node
        if node.t == 'heading':
            if entering:
                chunks = []
            else:
                slug = slugify.slugify(' '.join(chunks))
                new = commonmark.node.Node('html_inline', None)
                new.literal = f'<a id="{slug}"></a>'
                node.prepend_child(new)
            in_heading = entering
        elif in_heading and node.literal:
            chunks.append(node.literal)


def resolve_links(document: commonmark.node.Node, document_url: str, extension: str = '.html',
                  keep_extension: bool = True):
    # TODO: I have no idea if this will work with subdirectories, probably not.
    # TODO: This won't work with links to sections, e.g. about-me.md#interests
    for node, entering in document.walker():
        if entering:
            continue
        node: commonmark.node.Node
        if node.t == 'link':
            if re.match('^[a-z]+://', node.destination):
                continue
            node.destination = re.sub(r'\.md$', extension,
                                      urllib.parse.urljoin(document_url, node.destination))
            if not keep_extension:
                node.destination = re.sub(re.escape(extension) + '$', '', node.destination)
        if node.t == 'image':
            node.destination = urllib.parse.urljoin(document_url, node.destination)


def get_title(document: commonmark.node.Node) -> Optional[str]:
    in_title = False
    chunks = []
    for node, entering in document.walker():
        node: commonmark.node.Node
        if node.t == 'heading' and node.level == 1:
            if entering:
                chunks = []
            else:
                return ' '.join(chunks)
            in_title = entering
        elif in_title and node.literal:
            chunks.append(node.literal)
