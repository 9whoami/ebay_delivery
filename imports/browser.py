# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
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

    def __del__(self):
        self.close()

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

    def get_element_or_none(self, xpath: 'str or WebElement'):
        """
        Получение элемента по xpath
        :param xpath:
        :return:
        """
        if isinstance(xpath, WebElement):
            return xpath

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

    @staticmethod
    def get_element_info(web_element, attributes: 'list or str') -> list:
        if web_element is None:
            return None

        if isinstance(attributes, (list, tuple)):
            result = [web_element.get_attribute(attribute) for attribute in
                      attributes]
        elif isinstance(attributes, str):
            result = web_element.get_attribute(attributes)
        else:
            # result = None
            raise ValueError(
                "Expected 'list' or 'str' not {!r}".format(attributes))

        return result

    def get_text_from_element(self, xpath: str) -> str:
        web_element = self.get_element_or_none(xpath)
        inner_text = web_element.text if web_element else None
        return inner_text

    def filling_web_element(self, xpath: str, value: str,
                            name_attr: 'str or list' = None):
        web_element = self.get_element_or_none(xpath)
        if name_attr is None:
            name_attr = 'name', 'id',

        if not web_element:
            return False

        name = self.get_element_info(web_element, name_attr)

        try:
            try:
                web_element.clear()
            except Exception:
                pass
            web_element.send_keys(value)
            return True
        except Exception:
            return False

    def btn_click(self, xpath: str, screen: bool = True):
        if screen:
            self.take_screenshot()

        btn = self.get_element_or_none(xpath)
        if btn is None:
            return False

        try:
            btn.click()
            return True
        except Exception as e:
            return False

    def checkbox_checked(self, xpath: str):
        web_elem = self.get_element_or_none(xpath)
        if web_elem is None:
            return False

        checked = self.get_element_info(web_elem, 'checked')
        try:
            if checked:
                return True

            return self.btn_click(xpath, screen=False)
        except Exception as e:
            return False

    def selection(self, xpath, value):
        element = self.get_element_or_none(xpath)
        if element is None:
            return False

        try:
            select = Select(element)
            try:
                select.select_by_value(value)
            except Exception:
                select.select_by_visible_text(value)
            return True
        except Exception as e:
            return False
