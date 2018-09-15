import logging
import pathlib
import sys
import shutil

import builder

if __name__ != '__main__':
    raise RuntimeError("Why would you import this? Did you mean `builder.py`?")

RELEASE = 'release' in sys.argv
RELEASE = True

CONTENT = './content'
THEME = './theme'
ROOT_URL = 'https://aleshkev.github.io/' if RELEASE else './'
OUTPUT = '../'


logging.basicConfig(level=logging.INFO)

exclude = ('readme.md', 'source', '.git', '.gitignore', '.gitattributes', '.idea', 'requirements.txt',
           'LICENSE.md', 'README.md')
for o in pathlib.Path(OUTPUT).glob('*'):
    if o.name not in exclude:
        logging.info(f"Removing {o.absolute().resolve()}")
        if o.is_dir():
            shutil.rmtree(o)
        else:
            o.unlink()


builder.render(pathlib.Path(CONTENT), pathlib.Path(THEME), ROOT_URL, pathlib.Path(OUTPUT))
