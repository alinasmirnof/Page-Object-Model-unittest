import time
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login(self, user_email, user_pass, checkbox_btn = False):
       sign_in = self.driver.find_element(By.ID, LoginPageLocators.SignIn)
       sign_in.click()

       email_input = self.driver.find_element(By.NAME, 'USER_LOGIN')
       email_input.send_keys(user_email)

       pass_input = self.driver.find_element(By.NAME, 'USER_PASSWORD')
       pass_input.send_keys(user_pass)
       time.sleep(2)

       if checkbox_btn == True:
           remember_on = self.driver.find_element(By.ID, LoginPageLocators.RememberUser)
           remember_on.click()
       else:
           pass

       login_btn = self.driver.find_element(By.NAME, 'Login')
       login_btn.click()







