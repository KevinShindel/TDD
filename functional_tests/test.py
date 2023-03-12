import time
from unittest import main

from django.test import LiveServerTestCase
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from tools import create_browser


# use standart non-isolated db
# class NewVisitorTest(TestCase):
# use isolation db class
class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = create_browser()

    def tearDown(self) -> None:
        self.browser.close()
        self.browser.quit()

    def check_row_for_list_table(self, row_text):
        table = self.browser.find_element(by=By.ID, value='id_list_table')
        rows = table.find_elements(by=By.TAG_NAME, value='tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        url = 'http://127.0.0.1:8000/'
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
        time.sleep(1)
        # after page is reloaded, it contains: '1: Купить павлиньи перья'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_row_for_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element(by=By.ID, value='id_new_item')

        #  Текстовое поле по-прежнему приглашает ее добавить еще один элемент
        #  Она вводит Сделать мушку из павлиньи перьев
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #  Страница снова обновляется и теперь показывает оба элеиента
        self.check_row_for_list_table('1: Купить павлиньи перья')
        self.check_row_for_list_table('2: Сделать мушку из павлиньих перьев')

        #  Эдин интересно запомнит ли сайт ее список
        #  Далее Она видит что выводится небольшой текст с пояснениеми Она посещает этот адресс список по прежнему там

        #  Удовлетворенная она снова ложится спать


if __name__ == '__main__':
    main(warnings='ignore')
