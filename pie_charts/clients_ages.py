from locators import ClientsAgesLocators
from clients import Clients

class ClientsAges(Clients):
    def title_ages_presented(self):
        assert self.is_element_present(*ClientsAgesLocators.TITLE_AGE_OF_CLIENTS), "Title age of clients not presented"

    def pie_chart_ages_presented(self):
        assert self.is_element_present(*ClientsAgesLocators.PIE_CHART_AGE_OF_CLIENTS), "Pie chart age of clients not presented"

    def age_ranges_14_24(self):
        assert self.is_element_present(*ClientsAgesLocators.AGE_14_24), "AGE 14-24 not presented"

    def age_ranges_25_35(self):
        assert self.is_element_present(*ClientsAgesLocators.AGE_25_35), "AGE 25-35 not presented"

    def age_ranges_36_49(self):
        assert self.is_element_present(*ClientsAgesLocators.AGE_36_49), "AGE 36-49 not presented"

    def age_ranges_50_and_more(self):
        assert self.is_element_present(*ClientsAgesLocators.AGE_50_AND_MORE), "AGE 50 and more not presented"
