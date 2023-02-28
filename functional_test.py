from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


def test_main_page():
    executable_path = 'driver/chromedriver.exe'
    service = Service(executable_path=executable_path)
    browser = Chrome(service=service)
    url = 'http://127.0.0.1:8000/'
    browser.get(url=url)
    assert 'Django' in browser.page_source


if __name__ == '__main__':
    test_main_page()
