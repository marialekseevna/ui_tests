from locators import TimeOfPurchaseLocators
from clients import Clients

class TimeOfPurchase(Clients):
    def title_time_of_purchase_presented(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TITLE_TIME_OF_PURCHASE), "Title time of purchase presented"

    def pie_chart_time_of_purchase_presented(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.PIE_CHART_TIME_OF_PURCHASE), "Pie chart time of purchase presented"

    def time_0_9(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_0_9), "time 0-9 presented"

    def time_9_11(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_9_11), "time 9-11 presented"

    def time_11_13(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_11_13), "time 11-13 presented"

    def time_13_15(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_13_15), "time 13_15 presented"

    def time_15_17(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_15_17), "time 15_17 presented"

    def time_17_19(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_17_19), "time 17-19 presented"

    def time_19_24(self):
        assert self.is_element_present(*TimeOfPurchaseLocators.TIME_19_24), "time 19-24 presented"