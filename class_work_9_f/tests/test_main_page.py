import time

import pytest
import pytest_check as check
from class_work_9_f.page.locators import MainPage
import allure


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)


    check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаймому результату')
    check.is_true(page.btn_headers_mail.is_visible())

@allure.story('Тест для проверки input формы')
@allure.feature('Тест для провеки работоспособности инпута')

def test_headers(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookie.click

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_form.is_visible())

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_form.is_clickable())

    with allure.step('Проверка на ввод текста'):
        page.input_form.send_keys('nikita')
        page.button_click.click()
        time.sleep(10)


    #with allure.step('Проверка на ввод текста и проверка результата'):

    #    text_input_main = [
    #        "tatimati",
    #        "tatimati111111",
    #        "tatimati3232",
    #        "tatimati3333333",
    #    ]
    #    text_by_zone = page.text_by_zone.get.text()

    #    for text_input_main_elements in text_input_main:

    #        page.input_main_wrapper.send_keys(text_input_main_elements)
    #        page.btn_search_domain.click(1)

    #        time.sleep(5)

    #        check.equal(page.text_results_search_domain.get_text(), text_input_main_elements + text_by_zone)
    #        page.go_back()