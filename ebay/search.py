# -*- coding: utf-8 -*-
import settings as config
from imports.logger import Logger
from imports.exceptions import KeywordsError

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

        if not isinstance(self.keywords, str) or not self.keywords:
            raise KeywordsError("Не указан keywords!")

    def run(self):
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
        assert self.browser.btn_click(self.x_drop_menu)

        assert self.browser.btn_click(self.x_customize_btn)
        assert self.browser.btn_click(self.x_show_in)
        assert self.browser.btn_click(self.x_per_page)
        assert self.browser.checkbox_checked(self.x_seller_info)
        assert self.browser.btn_click(self.x_submit_custom)

    def _swith_post_to(self):
        assert self.browser.btn_click(self.x_lnk_post_to)
        assert self.browser.selection(self.x_post_to, self.state_value)
        assert self.browser.btn_click(self.x_go)
