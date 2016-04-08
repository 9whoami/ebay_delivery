# -*- coding: utf-8 -*-
from time import sleep

import settings as config
from imports.logger import Logger
from imports.exceptions import KeywordsError
from imports.exceptions import LinksToItemNotFoundError

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:55'
__description__ = """
Поиск товаров
"""


class Searching:
    def __init__(self, browser: "instance selenium.webdriver"):
        self.browser = browser
        self.url = config.urls['search']
        self.keywords = config.keywords
        self.state_value = str(config.state_value)
        self.logger = Logger()

        self.x_keywords = config.search_xpath['keywords']
        self.x_located = config.search_xpath['located']
        self.x_state = config.search_xpath['state']
        self.x_submit = config.search_xpath['submit']

        self.x_drop_menu = config.result_custom_xpath['drop_menu']
        self.x_lnk_post_to = config.result_custom_xpath['link_post_to']
        self.x_post_to = config.result_custom_xpath['post_to']
        self.x_go = config.result_custom_xpath['research']

        self.x_customize_btn = config.result_custom_xpath['result_custom']
        self.x_show_in = config.result_custom_xpath['show_in']
        self.x_per_page = config.result_custom_xpath['per_page']
        self.x_seller_info = config.result_custom_xpath['seller_info']
        self.x_submit_custom = config.result_custom_xpath['submit_custom']

        self.x_lnk_to_item = config.items_xpath['links_to_item']
        self.x_next_page = config.items_xpath['next_page']

        if not isinstance(self.keywords, str) or not self.keywords:
            raise KeywordsError("Не указан keywords!")

    def run(self):
        self.logger.info('Приступаем к поиску')
        try:
            self._search()
            # self._customize_result()
            self._swith_post_to()
        except AssertionError:
            return False
        else:
            return True

    def _search(self):
        self.browser.get(self.url)
        assert self.browser.filling_web_element(self.x_keywords, self.keywords)
        assert self.browser.btn_click(self.x_located, screen=False)
        assert self.browser.selection(self.x_state, self.state_value)
        assert self.browser.btn_click(self.x_submit)

    def _customize_result(self):
        assert self.browser.btn_click(self.x_drop_menu, screen=False)
        assert self.browser.btn_click(self.x_customize_btn, screen=False)
        assert self.browser.btn_click(self.x_show_in, screen=False)
        assert self.browser.btn_click(self.x_per_page, screen=False)
        assert self.browser.checkbox_checked(self.x_seller_info)
        assert self.browser.btn_click(self.x_submit_custom)

    def _swith_post_to(self):
        self.logger.info('Попытка изменить Postage to...')
        assert self.browser.btn_click(self.x_lnk_post_to, screen=False)
        assert self.browser.selection(self.x_post_to, self.state_value)
        assert self.browser.btn_click(self.x_go)

    def prepare_to_delivery(self):
        self.logger.info('Подготовка ссылок для рассылки')
        sleep(3)
        links_to_item = list()
        elements = self.browser.get_elements_by_xpath(self.x_lnk_to_item)
        if elements is None:
            raise LinksToItemNotFoundError

        while True:
            links_to_item += [
                self.browser.get_element_info(element, 'href')
                for element in elements]

            # aria-disabled="true"
            next_btn = self.browser.get_element_or_none(self.x_next_page)
            if next_btn.get_attribute('aria-disabled'):
                break

            self.browser.btn_click(next_btn)
            sleep(3)

            elements = self.browser.get_elements_by_xpath(self.x_lnk_to_item)
        self.logger.info('{} товаров найдено'.format(len(links_to_item)))
        for cnt, link_to_item in enumerate(links_to_item):
            self.logger.info(
                'Обрабатываем {}/{}'.format(cnt, len(links_to_item)))
            yield link_to_item

