#!/usr/bin/python3
# -*- coding: utf-8 -*-
from imports.logger import Logger

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:46'
__description__ = """
Главный скрипт проекта, которые и следует запускать.
"""
logger = Logger()


def main():
    logger.debug("This is debug message")


if __name__ in "__main__":
    main()
