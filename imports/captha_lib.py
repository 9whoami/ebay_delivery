# -*- coding: utf-8 -*-
from PIL import Image
from antigate import AntiGate
from imports.logger import Logger
from imports.config_read import read_cfg
import settings as conf

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '30.03.16 3:38'
__description__ = """
Description for the python module
"""
logger = Logger()


class RecognizeCaptcha(AntiGate):
    def __init__(self):
        super().__init__(send_config={'numeric': '1'}, auto_run=False,
                         **read_cfg(**conf.antigate_conf))

    @staticmethod
    def crop_image(image_name, captcha_size):
        image = Image.open(conf.screen_dir + image_name)
        image.crop(captcha_size).save(conf.temp_dir + image_name)

    def _balance(self):
        balanse = super().balance()
        logger.info("Баланс антикаптчи: {}".format(balanse))
        if balanse < 1:
            raise RuntimeWarning('Пополните баланс сервиса антикапчи')

    def recognize(self, image: str, captcha_size: tuple):
        try:
            self.balance()
        except RuntimeWarning:
            return None

        self.crop_image(image, captcha_size)
        super().run(conf.temp_dir + image)

