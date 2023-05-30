import pytest
from selene import browser
from selenium import webdriver
from selene.support.shared.jquery_style import s

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

desktop_sizes = [(1920, 1080), (1366, 768)]
mobile_sizes = [(360, 800), (414, 896)]

desktop_only = pytest.mark.parametrize(
    'web_browser', desktop_sizes, indirect=True
)
mobile_only = pytest.mark.parametrize(
    'web_browser', mobile_sizes, indirect=True
)


@pytest.fixture(params=desktop_sizes + mobile_sizes)
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    yield browser

    browser.quit()


@desktop_only
def test_github_desktop(web_browser):
    browser.open('https://github.com')
    s('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(web_browser):
    browser.open('https://github.com')
    s('.flex-column [aria-label="Toggle navigation"]').click()
    s('[href="/login"]').click()
