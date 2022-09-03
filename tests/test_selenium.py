
#   Разобрал и воспроизвел данный тест, но запустить не удалось.
# self.driver.find_element_by_name  и  self.driver.find_element_by_css_selector
# вылезает сообщение (Unresolved attribute reference 'find_element_by_name' for class 'WebDriver' ).
# В чем может быть проблема?

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


LOGIN = ''
PASSWORD = ''

class TestAuthYA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome('C:\Users\budar\Downloads\chromedriver_win32\chromedriver.exe')

    def test_login_success(self):
        self.driver.get('https://passport.yandex.ru/auth/')
        self.assertIn('Авторизация', self.driver.title)
        elem = self.driver.find_element_by_name('login')
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_css_selector(
            "input#passp-field-passwd")
        elem.send_keys(PASSWORD)
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



# class TestAuthYA(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome('C:\Users\budar\Downloads\chromedriver_win32\chromedriver.exe')
#         self.driver.get('https://passport.yandex.ru/auth/')
#
#     def test_01(self):
#         driver = self.driver
#         self.assertIn('Авторизация', self.driver.title)
#         elem = self.driver.find_element_by_name('login')
#         driver.send
