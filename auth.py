import time
from locators import LoginLocators
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

class Auth():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def successful_auth(self):
        self.browser.get(self.url)
        # перед запуском вставить login and password
        self.lgn = ""
        self.psw = ""
        try:
            #перед запуском вставить title
            assert "" in self.browser.title

            # input login
            login = self.browser.find_element(*LoginLocators.LOGIN)
            login.send_keys(self.lgn)

            # input password
            password = self.browser.find_element(*LoginLocators.PASSWORD)
            password.send_keys(self.psw)

            # enter button for auth
            button = self.browser.find_element(*LoginLocators.AUTH_BUTTON)
            button.click()
            time.sleep(1)
        except ValueError as err:
            self.browser.driver.quit()  #close browser
