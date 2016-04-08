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
    post_to=".//*[@name='_fcid']",
    research=".//*[@value='Go']",

    result_custom=".//*[@id='custLink']",
    show_in=".//*[@id='e1-1']/div/table/tbody/tr[1]/td[2]/label[1]/input",
    per_page=".//*[@id='e1-1']/div/table/tbody/tr[4]/td[2]/label[4]/input",
    seller_info=".//*[@id='e1-13']",
    submit_custom=".//*[@id='e1-3']",
)

items_xpath = dict(
    links_to_item=".//a[@class='vip']",
    next_page=".//a[@aria-label='Next page of results']",

    contact_lnk=".//a[text()='contact seller']",
    topic=".//input[@value='5']",
    contact_btn=".//*[@id='contactSeller']",

    seller_name=".//*[@id='RightSummaryPanel']/.//a/span[@class='mbg-nw']",
)

contact_xpath = dict(
    topic=".//*[@id='qusetOther_cnt_cnt']",
    msg=".//*[@id='msg_cnt_cnt']",
    captha_edit=".//*[@id='tokenText']",
    send_btn=".//*[@id='sendBtn']",

    topic_error=".//*[@id='qusetOther_cnt_cnt_errhlp_li']",
    msg_error=".//*[@id='msg_cnt_cnt_errhlp_li']",
    captcha_error=".//*[@id='v4-11']/div[1]",

    denied=".//*[@id='CentralArea']/.//div[@class='sm-co']"
           "/table/tbody/tr/td[2]/div",
    success=".//*[@id='CentralArea']/.//p[@class='sm-md']",
)

urls = dict(
    login='https://signin.ebay.co.uk/ws/eBayISAPI.dll?SignIn&ru=http%3A%2F%2Fwww.ebay.co.uk%2F',
    redirect_after_login="http://www.ebay.co.uk/",
    search="http://www.ebay.co.uk/sch/ebayadvsearch",
)

