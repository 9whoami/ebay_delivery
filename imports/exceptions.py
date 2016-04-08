# -*- coding: utf-8 -*-
from .logger import Logger

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:56'
__description__ = """
Исключения вызываемые проектом
"""


class BaseError(Exception):
    def __init__(self, message):
        if message is None:
            message = self.__class__.__name__
        self.message = message
        self.logger = Logger()

    def __str__(self):
        self.logger.error(self.message)
        return str()


class SigninError(BaseError):
    def __init__(self, message=None):
        super().__init__(message)


class KeywordsError(BaseError):
    def __init__(self, message=None):
        super().__init__(message)


class LinksToItemNotFoundError(BaseError):
    def __init__(self, message=None):
        super().__init__(message)


class SendMessageError(BaseError):
    def __init__(self, message=None):
        super().__init__(message)

