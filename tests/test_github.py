import allure
import pytest
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.fixture(scope='session', autouse=True)
def browser_init():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config._hold_browser_open = True


def test_github():

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репоситорий'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step(f'Проверяем наличие Issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
