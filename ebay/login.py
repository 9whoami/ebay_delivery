# -*- coding: utf-8 -*-
import settings as config
from imports.captha_lib import RecognizeCaptcha
from imports.logger import Logger

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:55'
__description__ = """
Вход в аккаунт
"""
logger = Logger()


class Signin:
    def __init__(self, browser: 'instance selenium.webdriver',
                 login: str, password: str, auto_start: bool = False):
        self.browser = browser
        self.login = login
        self.password = password

        if auto_start:
            self.run()

    def run(self):
        login_url = config.urls['login']
        self.browser.get(login_url)
        try:
            assert self.recognize_captha()
            assert self.fill_login()
            assert self.fill_passwd()
            self.submit_form()
            assert self.check_signin()
            logger.info("Вошли на сайт")
            return True
        except AssertionError:
            logger.error('Не удалось войти на сайт')
            return False

    def fill_login(self):
        xpath = config.login_xpath['login']

        return self.browser.filling_web_element(xpath, self.login)

    def fill_passwd(self):
        xpath = config.login_xpath['passwd']

        return self.browser.filling_web_element(xpath, self.password)

    def submit_form(self):
        xpath = config.login_xpath['submit']

        return self.browser.btn_click(xpath)

    def recognize_captha(self):
        xpath_to_captha = config.login_xpath['captcha']
        xpath_to_captcha_edit = config.login_xpath['captcha_edit']

        if not self.browser.get_element_or_none(xpath_to_captha):
            return True

        scr_name = self.browser.take_screenshot()
        recaptcha = RecognizeCaptcha()
        recaptcha.recognize(scr_name)
        if recaptcha.captcha_result:
            return self.browser.filling_web_element(xpath_to_captcha_edit,
                                                    recaptcha.captcha_result)
        else:
            return False

    def check_signin(self):
        xpath_to_error_text = config.login_xpath['error']
        xpath_to_my_name = config.login_xpath['my_name']
        redirect_url = config.urls['redirect_after_login']

        err_text = self.browser.get_text_from_element(xpath_to_error_text)
        if err_text:
            print(err_text)
            return False

        self.browser.get(redirect_url)
        return self.browser.get_text_from_element(xpath_to_my_name)
