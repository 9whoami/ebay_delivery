#!/usr/bin/python3
# -*- coding: utf-8 -*-
import settings as conf
from sys import exit
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
    logger.info('Чтение файла с аккаунтами')
    with open(conf.accounts_file, 'r') as f:
        file_buffer = [line for line in f]

    account = file_buffer.pop()

    # TODO for test
    # with open(conf.accounts_file, 'w') as f:
    #     for line in file_buffer:
    #         f.writelines(line)

    return account.split(':')


def main():
    try:
        login, passwd = get_accounts()
        logger.info('Login: {!r}, Password: {!r}'.format(login, passwd))
        browser = WebDriver()
        logger.info('Запущен браузер')

        signin = Signin(browser, login, passwd)

    except Exception as e:
        logger.error('Работа программы завершена с сообщением {!r}'.format(e))
        exit()

    try:
        assert signin.run()
    except AssertionError:
        exit()



if __name__ in "__main__":
    main()
