from locators import NumberOfPurchasesLocators
from clients import Clients

class NumberOfPurchases(Clients):
    def title_number_of_purchases_presented(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.TITLE_NUMBER_OF_PURCHASES), "Title number of purchases presented"

    def pie_chart_number_of_purchases_presented(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PIE_CHART_NUMBER_OF_PURCHASES), "Pie chart number of purchases presented"

    def purchase_1(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PURCHASE_1), "1 purchase presented"

    def purchase_2(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PURCHASE_2), "2 purchases presented"

    def purchase_3(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PURCHASE_3), "3 purchases presented"

    def purchase_4(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PURCHASE_4), "4 purchases presented"

    def purchase_5_and_more(self):
        assert self.is_element_present(*NumberOfPurchasesLocators.PURCHASE_5_AND_MORE), "5 and more purchases presented"