from base_page import BasePage
import time
from locators import LoginLocators
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

class Auth(BasePage):
    def successful_auth(self):
        self.driver.get(self.base_url)
        # перед запуском вставить login and password
        self.lgn = ""
        self.psw = ""
        try:
            #перед запуском вставить title
            assert "" in self.driver.title

            # input login
            login = self.driver.find_element(*LoginLocators.LOGIN)
            login.send_keys(self.lgn)

            # input password
            password = self.driver.find_element(*LoginLocators.PASSWORD)
            password.send_keys(self.psw)

            # enter button for auth
            button = self.driver.find_element(*LoginLocators.AUTH_BUTTON)
            button.click()
            time.sleep(1)
        except ValueError as err:
            self.driver.quit()  #close browser
