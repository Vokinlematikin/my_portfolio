import os

from class_work_9_f.page.base_page import WebPage
from class_work_9_f.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://hoster.by'

        super().__init__(web_driver, url)

    btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')
    btn_headers_hosting = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Хостинг")]')
    btn_headers_cloud = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Облако")]')
    btn_headers_mail = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Почта")]')
    btn_pip_up_cookie = WebElement(xpath='//*[@id="accept"]')
    input_form = WebElement(xpath='//*[@placeholder="Введите домены"]')
    button_click = WebElement(xpath='/html/body/div[8]/div[1]/div[1]/div/div[1]/div[2]/div[2]/button/span')
