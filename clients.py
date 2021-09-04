from base_page import BasePage
from locators import ClientsLocators
from selenium.common.exceptions import NoSuchElementException
import time


class Clients(BasePage):

    def go_to_clients(self):
        self.driver.get(self.base_url)
        clients = self.driver.find_element(*ClientsLocators.CLIENTS_BUTTON)
        clients.click()
        time.sleep(5)