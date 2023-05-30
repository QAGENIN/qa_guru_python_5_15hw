import pytest
from selene import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest

desktop_windows_size = [(1920, 1080), (1366, 768)]
mobile_windows_size = [(360, 800), (414, 896)]


@pytest.fixture(params=desktop_windows_size)
def desktop_window_size(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser

    browser.quit()


def test_github_desktop(desktop_window_size):
    browser.open('https://github.com')
    s('.HeaderMenu-link--sign-in').click()


@pytest.fixture(params=mobile_windows_size)
def mobile_windows_size(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser

    browser.quit()


def test_github_mobile(mobile_windows_size):
    browser.open('https://github.com')
    s('.flex-column [aria-label="Toggle navigation"]').click()
    s('[href="/login"]').click()
