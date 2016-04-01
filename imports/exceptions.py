# -*- coding: utf-8 -*-
from .logger import Logger

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:56'
__description__ = """
Исключения вызываемые проектом
"""


class BaseError(Exception):
    def __init__(self):
        self.message = None
        self.logger = Logger()

    def __str__(self):
        self.logger.error(self.message)
        return str()


class SigninError(BaseError):
    def __init__(self, msg):
        super().__init__()
        self.message = msg


class KeywordsError(BaseError):
    def __init__(self, message):
        super().__init__()
        self.message = message
