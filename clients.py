from locators import ClientsLocators
from selenium.common.exceptions import NoSuchElementException
import time


class Clients():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_clients(self):
        self.browser.get(self.url)
        clients = self.browser.find_element(*ClientsLocators.CLIENTS_BUTTON)
        clients.click()
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True