import unittest
from selenium import webdriver
from page_objects.login_page import LoginPage
from config import URLS, Credentials
import time

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
        cls.driver.get(URLS.URL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login(Credentials.EmailData, Credentials.PasswordData, checkbox_btn=True)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main