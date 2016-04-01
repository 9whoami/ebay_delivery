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

search_xpath = dict(
    keywords=".//*[@id='_nkw']",
    located=".//*[@id='LH_LocatedInRadio']",
    state=".//*[@id='_salicSelect']",
    submit=".//*[@id='searchBtnLowerLnk']",
)

result_custom_xpath = dict(
    drop_menu=".//*[@id='viewType']",
    link_post_to=".//*[@id='loczip']/a",
    post_to=".//*[@id='zip_e1-48']",
    research=".//*[@id='zip_e1-55']",

    result_custom=".//*[@id='custLink']",
    show_in=".//*[@id='e1-1']/div/table/tbody/tr[1]/td[2]/label[1]/input",
    per_page=".//*[@id='e1-1']/div/table/tbody/tr[4]/td[2]/label[4]/input",
    seller_info=".//*[@id='e1-13']",
    submit_custom=".//*[@id='e1-3']",
)

urls = dict(
    login='https://signin.ebay.co.uk/ws/eBayISAPI.dll?SignIn&ru=http%3A%2F%2Fwww.ebay.co.uk%2F',
    redirect_after_login="http://www.ebay.co.uk/",
    search="http://www.ebay.co.uk/sch/ebayadvsearch",
)
