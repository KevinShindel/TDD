from selenium.webdriver import Chrome

from selenium.webdriver.chrome.service import Service


def create_browser():
    executable_path = 'driver/chromedriver.exe'
    service = Service(executable_path=executable_path)
    browser = Chrome(service=service)
    return browser
