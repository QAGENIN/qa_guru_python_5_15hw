import pytest
from selene import browser
from selenium import webdriver
from selene.support.shared.jquery_style import s

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

desktop_windows_sizes = [(1920, 1080), (1366, 768)]
mobile_windows_sizes = [(360, 800), (414, 896)]

windows_sizes = [
    pytest.param(size, id='desktop') for size in desktop_windows_sizes
] + [pytest.param(size, id='mobile') for size in mobile_windows_sizes]


@pytest.fixture(params=windows_sizes)
def web_browser(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    yield browser

    browser.quit()


def test_github_desktop(web_browser, request):
    if 'mobile' in request.node.name:
        pytest.skip('Разрешение не подходит для мобильных устройств')

    browser.open('https://github.com')
    s('.HeaderMenu-link--sign-in').click()


def test_github_mobile(web_browser, request):
    if 'desktop' in request.node.name:
        pytest.skip('Разрешение не подходит для вашего устройства')

    browser.open('https://github.com')
    s('.flex-column [aria-label="Toggle navigation"]').click()
    s('[href="/login"]').click()
