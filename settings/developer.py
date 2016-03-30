# -*- coding: utf-8 -*-

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '27.03.16 0:54'
__description__ = """
Настройки разработчика.
"""

antigate_conf = dict(file='antigate.conf', section='default')

login_xpath = dict(
    login=".//input[@type='text']",
    passwd=".//*[@placeholder='Password']",
    submit=".//*[@id='sgnBt']",

    error=".//*[@id='errf']",
    my_name=".//*[@id='gh-ug']/b[1]",
    captcha=".//iframe[@id='frameBot_img']",
    captcha_edit = ".//*[@id='tokenText']"
)

urls = dict(
    login='https://signin.ebay.co.uk/ws/eBayISAPI.dll?SignIn&ru=http%3A%2F%2Fwww.ebay.co.uk%2F',
    redirect_after_login="http://www.ebay.co.uk/",
)
