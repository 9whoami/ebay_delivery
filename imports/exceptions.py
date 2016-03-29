# -*- coding: utf-8 -*-

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:56'
__description__ = """
Исключения вызываемые проектом
"""


class SigninError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
