# -*- coding: utf-8 -*-

from os import getcwd
from os import sep
from os.path import isdir
from sys import exit

try:
    from .base import *
    from .advanced import *
    from .developer import *
except Exception as e:
    exit(e)

if not log_dir.endswith(sep):
    log_dir += sep

if not log_dir.startswith(sep):
    log_dir = sep + log_dir

if not isdir(log_dir):
    log_dir = getcwd() + log_dir
