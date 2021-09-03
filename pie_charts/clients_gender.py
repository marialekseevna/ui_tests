from locators import ClientGenderLocators
from clients import Clients

class ClientGender(Clients):
    def title_gender_presented(self):
        self.is_element_present(*ClientGenderLocators.TITLE_GENDER_OF_CLIENTS), "Title gender of clients presented"

    def pie_chart_gender_presented(self):
        self.is_element_present(*ClientGenderLocators.PIE_CHART_GENDER_OF_CLIENTS), "Pie chart gender of clients presented"

    def gender_male(self):
        self.is_element_present(*ClientGenderLocators.GENDER_MALE), "Gender male presented"

    def gender_female(self):
        self.is_element_present(*ClientGenderLocators.GENDER_FEMALE), "Gender female presented"