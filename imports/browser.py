# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
import settings as config

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:46'
__description__ = """
Обертка для selenium.webdriver
"""


class SwithSuperMetaclass(type):
    """
    Метакласс для подметы класса родителя для класса WebDriver.
    """

    def __new__(cls, name, bases, dct):
        if cls.web_driver_select():
            bases = webdriver.PhantomJS,
        else:
            bases = webdriver.Firefox,

        return type.__new__(cls, name, bases, dct)

    @staticmethod
    def web_driver_select():
        web_drivers = {config.PhantomJS: 1, config.Firefox: 0}
        try:
            return web_drivers[config.web_driver]
        except KeyError:
            raise SystemExit("Укажите правильный параметр web driver")


class WebDriver(metaclass=SwithSuperMetaclass):
    """
    Обертка для selenium.webdriver
    """

    def __init__(self):
        super().__init__(**self.driver_profile)

    @property
    def driver_profile(self):
        if SwithSuperMetaclass.web_driver_select():
            dcap = dict(DesiredCapabilities.PHANTOMJS).copy()
            service_args = config.service_args if \
                isinstance(config.service_args, list) else list()
            profile = dict(desired_capabilities=dcap,
                           service_args=service_args)
        else:
            ff_profile = webdriver.FirefoxProfile()
            profile = dict(firefox_profile=ff_profile)
        return profile

    def _get_element(self, locator_strategies, locator):
        """
        Ищет элемент на странице с неявным ожиданием его появления.
        Если в течение ожидания элемент не появился возвращается None
        :param locator_strategies:
        :param locator:
        :return:
        """
        try:
            element = WebDriverWait(self, config.explicit_waits).until(
                EC.presence_of_element_located((locator_strategies, locator)))
        except TimeoutException:
            element = None
        return element

    def get_element_or_none(self, xpath):
        """
        Получение элемента по xpath
        :param xpath:
        :return:
        """
        element = self._get_element(By.XPATH, xpath)
        return element

    def find_element_by_partial_link(self, link_text):
        """
        Получение элементы по части названия.
        :param link_text:
        :return:
        """
        element = self._get_element(By.PARTIAL_LINK_TEXT, link_text)
        return element

    def take_screenshot(self):
        file_name = '{}.png'.format(str(datetime.now()))
        try:
            self.save_screenshot(config.log_dir + file_name)
        except:
            return None
        return file_name

    def get(self, url):
        """
        Загрузка страницы с повторением при неудаче
        :param url:
        :return:
        """
        for i in range(0, 4):
            timeout = config.load_timeout + i * 10
            try:
                self.set_page_load_timeout(timeout)
                self._get(url)

                self.set_page_load_timeout(config.load_timeout)
                return True
            except Exception:
                continue

    def _get(self, url):
        is_not_load = lambda page_source: load_error in page_source or \
                                          blank_source in page_source
        load_error = '<!ENTITY loadError.label "Проблема при загрузке страницы">'
        blank_source = '<html><head></head><body></body></html>'

        super().get(url)

        result = self.page_source
        self.take_screenshot()

        if is_not_load(result):
            raise Exception

        return result

    def get_elements_by_xpath(self, xpath):
        """
        Получение списка элементов по xpath
        :param xpath:
        :return:
        """
        try:
            elements = self.find_elements_by_xpath(xpath)
        except Exception:
            elements = []
        return elements

    def __del__(self):
        self.close()
