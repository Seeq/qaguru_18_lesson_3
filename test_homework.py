
import pytest
from selene import browser, be, have

@pytest.fixture(scope="session")
def browser_url():
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()

@pytest.fixture(scope="session")
def browser_res():
    browser.config.window_height = '2560'
    browser.config.window_width = '1440'

def test_search(browser_url, browser_res):
    browser.element('[id="searchbox_input"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search_no_results(browser_url, browser_res):
    browser.element('[id="search_form_input"]').clear().type('атуцшоатуцшатушаиуцаицуш').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))