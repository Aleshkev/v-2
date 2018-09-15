import logging
import pathlib
import sys
import shutil

import builder

if __name__ != '__main__':
    raise RuntimeError("Why would you import this? Did you mean `builder.py`?")

RELEASE = True

CONTENT = './content'
THEME = './theme'
ROOT_URL = 'https://aleshkev.github.io/a/' if RELEASE else './'
OUTPUT = '../a/'


logging.basicConfig(level=logging.INFO)

try:
    shutil.rmtree(OUTPUT)
except FileNotFoundError:
    pass


builder.render(pathlib.Path(CONTENT), pathlib.Path(THEME), ROOT_URL, pathlib.Path(OUTPUT))
