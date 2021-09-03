from locators import DayOfPurchaseLocators
from clients import Clients

class DayOfPurchase(Clients):
    def title_day_of_purchase_presented(self):
        assert self.is_element_present(*DayOfPurchaseLocators.TITLE_DAY_OF_PURCHASE), "Title day of purchase presented"

    def pie_chart_day_of_purchase_presented(self):
        assert self.is_element_present(*DayOfPurchaseLocators.PIE_CHART_DAY_OF_PURCHASE), "Pie chart day of purchase presented"

    def monday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.MONDAY), "monday presented"

    def tuesday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.TUESDAY), "tuesday presented"

    def wednesday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.WEDNESDAY), "wednesday presented"

    def thursday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.THURSDAY), "thursday presented"

    def friday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.FRIDAY), "friday presented"

    def saturday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.SATURDAY), "saturday presented"

    def sunday(self):
        assert self.is_element_present(*DayOfPurchaseLocators.SUNDAY), "sunday presented"