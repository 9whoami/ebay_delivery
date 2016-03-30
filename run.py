#!/usr/bin/python3
# -*- coding: utf-8 -*-
from imports.logger import Logger
from imports.browser import WebDriver
from ebay.login import Signin

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:46'
__description__ = """
Главный скрипт проекта, которые и следует запускать.
"""
logger = Logger()


def get_accounts():
    with open('accounts.txt', 'r') as f:
        file_buffer = [line for line in f]

    account = file_buffer.pop()

    # TODO for test
    # with open('accounts.txt', 'w') as f:
    #     for line in file_buffer:
    #         f.writelines(line)

    return account.split(':')


def main():
    logger.debug("This is debug message")
    login, passwd = get_accounts()
    browser = WebDriver()
    signin = Signin(browser, login, passwd)
    signin.run()


if __name__ in "__main__":
    main()
