import os

from class_work_9_f.page.base_page import WebPage
from class_work_9_f.page.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://lostfilm.tv'

        super().__init__(web_driver, url)

    btn_headers_series = WebElement(xpath='//div[3]/div[1]/div/div[1]/div/a[1]/span[1],"СЕРИАЛЫ")]')
    btn_headers_movies = WebElement(xpath='//div[3]/div[1]/div/div[1]/div/a[2]/span[1],"КИНО")]')
    btn_headers_news = WebElement(xpath='//div[3]/div[1]/div/div[1]/div/a[3]/span[1],"НОВОСТИ")]')
    btn_headers_video = WebElement(xpath='//div[3]/div[1]/div/div[1]/div/a[4]/span[1],"ВИДЕО")]')
    btn_headers_new = WebElement(xpath='/div[3]/div[1]/div/div[1]/div/a[5]/span[1],"НОВИНКИ)]')
    btn_headers_schedule = WebElement(xpath='//div[3]/div[1]/div/div[1]/div/a[6]/span[1],"РАСПИСАНИЕ")]')

    btn_footers_series = WebElement(xpath='//div[4]/div/div[1]/a[1],"Сериалы")]')
    btn_footers_news = WebElement(xpath='//div[4]/div/div[1]/a[2],"Новости")]')
    btn_footers_new = WebElement(xpath='//div[4]/div/div[1]/a[3],"Новинки")]')
    btn_footers_video = WebElement(xpath='/div[4]/div/div[1]/a[4],"Видео")]')
    btn_footers_schedule = WebElement(xpath='/div[4]/div/div[1]/a[5],"Расписание)]')
    btn_footers_official = WebElement(xpath='//div[4]/div/div[1]/a[6],"Официальная группа VK")]')
    btn_footers_about = WebElement(xpath='//div[4]/div/div[2]/a[1],"О проекте)]')
    btn_footers_rules = WebElement(xpath='//div[4]/div/div[2]/a[2],"Правила")]')
    btn_footers_faq = WebElement(xpath='/div[4]/div/div[2]/a[3],"FAQ")]')
    btn_footers_reklama = WebElement(xpath='//div[4]/div/div[2]/a[4],"Размещение рекламы")]')
    btn_footers_feedback = WebElement(xpath='//div[4]/div/div[2]/a[5],"Обратная связь)]')
    btn_footers_rss = WebElement(xpath='//div[4]/div/div[2]/a[6],"RSS")]')


