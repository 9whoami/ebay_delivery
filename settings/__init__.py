# -*- coding: utf-8 -*-

from os import getcwd
from os import sep
from os.path import isdir
from os.path import isfile
from sys import exit

try:
    from .base import *
    from .advanced import *
    from .developer import *
except Exception as e:
    exit(e)


def _prepare_path(path):

    if not path.endswith(sep):
        path += sep

    if not path.startswith(sep):
        path = sep + path

    if not isdir(path):
        path = getcwd() + path

    return path


def _prepare_file(file):
    if not file.startswith(sep):
        file = sep + file

    if not isfile(file):
        file = getcwd() + file

    return file

log_dir = _prepare_path(log_dir)
temp_dir = _prepare_path(temp_dir)
screen_dir = _prepare_path(screen_dir)
seller_cache = _prepare_file(seller_cache)
