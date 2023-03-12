import time
import warnings
from unittest import main

from django.test import LiveServerTestCase
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from tools import create_browser


class NewVisitorTest(LiveServerTestCase):

    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = create_browser()

    def tearDown(self) -> None:
        self.browser.close()
        self.browser.quit()

    def wait_for_row_int_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(by=By.ID, value='id_list_table')
                rows = table.find_elements(by=By.TAG_NAME, value='tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_row_for_list_table(self, row_text):
        warnings.warn(f"The '{self.__class__.check_row_for_list_table.__name__}' "
                      f"is deprecated use  'wait_for_row_int_table'", DeprecationWarning)
        table = self.browser.find_element(by=By.ID, value='id_list_table')
        rows = table.find_elements(by=By.TAG_NAME, value='tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # url = 'http://127.0.0.1:8000/'
        # Эдит слышала про крутое онлайн-приложение со списком неотложных дел. Она решает посетить его
        # self.browser.get(url=url)
        # use test class included url
        self.browser.get(self.live_server_url)

        # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(by=By.TAG_NAME, value='h1')
        self.assertIn('To-Do', header_text.text, )

        #  ей сразу предлагают ввести элемент списка
        inputbox = self.browser.find_element(by=By.ID, value='id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #  Она набирает в текстовом поле 'Купить павлиньи перья' в качестве элемента списка
        inputbox.send_keys('Купить павлиньи перья')

        # after page is reloaded, it contains: '1: Купить павлиньи перья'
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_int_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element(by=By.ID, value='id_new_item')

        #  Текстовое поле по-прежнему приглашает ее добавить еще один элемент
        #  Она вводит Сделать мушку из павлиньи перьев
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)

        #  Страница снова обновляется и теперь показывает оба элеиента
        self.wait_for_row_int_table('1: Купить павлиньи перья')
        self.wait_for_row_int_table('2: Сделать мушку из павлиньих перьев')

        #  Эдин интересно запомнит ли сайт ее список
        #  Далее Она видит что выводится небольшой текст с пояснениеми Она посещает этот адресс список по прежнему там

        #  Удовлетворенная она снова ложится спать


if __name__ == '__main__':
    main(warnings='ignore')
