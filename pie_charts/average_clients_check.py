from locators import AverageClientsCheckLocators
from clients import Clients

class AverageClientsCheck(Clients):
    def title_average_clients_check_presented(self):
        assert self.is_element_present(*AverageClientsCheckLocators.TITLE_AVERAGE_CLIENTS_CHECK), "Title average clients check not presented"

    def pie_chart_average_clients_check_presented(self):
        assert self.is_element_present(*AverageClientsCheckLocators.PIE_CHART_AVERAGE_CLIENTS_CHECK), "Pie chart average clients check not presented"

    def check_up_to_300(self):
        assert self.is_element_present(*AverageClientsCheckLocators.CHECK_UP_TO_300), "Check up to 300 not presented"

    def check_300_600(self):
        assert self.is_element_present(*AverageClientsCheckLocators.CHECK_300_600), "Check 300-600 not presented"

    def check_600_1000(self):
        assert self.is_element_present(*AverageClientsCheckLocators.CHECK_600_1000), "Check 600-1000 not presented"

    def check_1000_1500(self):
        assert self.is_element_present(*AverageClientsCheckLocators.CHECK_1000_1500), "Check 1000-1500 not presented"

    def check_1500_and_more(self):
        assert self.is_element_present(*AverageClientsCheckLocators.CHECK_1500_AND_MORE), "Check 1500 and more not presented"