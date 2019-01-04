import logging
import pathlib
import sys
import shutil

import htmlmin
import csscompressor

from script import md_builder
from script import adoc_builder

if __name__ != '__main__':
    raise RuntimeError("Shouldn't be imported.")

RELEASE = 'release' in sys.argv

CONTENT = './content'
MD_THEME = './theme'
ROOT_URL = 'https://aleshkev.github.io/a/' if RELEASE else './'
OUTPUT = './a/'

logging.basicConfig(level=logging.INFO)

try:
    shutil.rmtree(OUTPUT)
except FileNotFoundError:
    pass


def main(content, md_theme, root_url, output):
    md_builder.render(content, md_theme, root_url, output, not RELEASE)
    adoc_builder.render(content, root_url, output)

    exclude = ('nav.md', 'footer.md', 'site-name.txt')
    exclude_suffixes = ('.md', '.adoc', '.css', '.scss')

    for file in content.glob('*'):
        if file.suffix in exclude_suffixes or file.name in exclude:
            continue
        logging.info(f"Copying {file}")
        shutil.copy(str(file), str(output / file.name))

    for file in output.glob('*.html'):
        logging.info(f"Minifying {file}")
        file.write_text(htmlmin.minify(file.read_text(encoding='utf-8')), encoding='utf-8')

    for file in output.glob('*.css'):
        if file.name.endswith('.min.css'):
            continue
        logging.info(f"Minifying {file}")
        file.write_text(csscompressor.compress(file.read_text()))


main(pathlib.Path(CONTENT), pathlib.Path(MD_THEME), ROOT_URL, pathlib.Path(OUTPUT))
