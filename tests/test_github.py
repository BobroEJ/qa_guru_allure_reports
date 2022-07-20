import allure
import pytest
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.fixture(scope='session', autouse=True)
def browser_init():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config._hold_browser_open = True


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.feature('Задачи в репозитории')
@allure.story('Проверяем видимость Issue #76, чистый селен')
@allure.link('https://github.com/', name='Testing')
def test_selene():

    browser.open('https://github.com/')

    browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#76')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.feature('Задачи в репозитории')
@allure.story('Проверяем видимость Issue #76, используем with allure.step')
@allure.link('https://github.com/', name='Testing')
def test_dynamic_steps():

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step(f'Проверяем наличие Issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.feature('Задачи в репозитории')
@allure.story('Проверяем видимость Issue #76, используем @allure.step')
@allure.link('https://github.com/', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number(76)


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def search_for_repository(repo):
    browser.element('.header-search-input').type(repo).press_enter()


@allure.step('Переходим по ссылке репозитория')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(f'#{number}')).should(be.visible)
