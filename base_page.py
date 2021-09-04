from locators import ClientsLocators
from selenium.common.exceptions import NoSuchElementException
import time

class BasePage:

    def __init__(self, browser, driver, timeout=10):
        self.browser = browser
        self.driver = driver
        self.base_url = ""
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True