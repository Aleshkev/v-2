
from os import system
from pathlib import Path

system("hugo")
system("push-dir --dir=public --branch=master --cleanup --verbose --allow-unclean")
