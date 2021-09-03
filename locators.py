from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN = (By.ID, "login")
    PASSWORD = (By.ID, "password")
    AUTH_BUTTON = (By.CLASS_NAME, "auth__action--login")

class ClientsLocators:
    CLIENTS_BUTTON = (By.CSS_SELECTOR, "app-clients-icon")

class ClientsAgesLocators:
    TITLE_AGE_OF_CLIENTS = (By.XPATH, "//p[contains(.,'Возраст клиентов')]")
    PIE_CHART_AGE_OF_CLIENTS = (By.ID, "ageData")
    AGE_14_24 = (By.XPATH, "//td[2]/div")
    AGE_25_35 = (By.XPATH, "//tr[2]/td[2]/div")
    AGE_36_49 = (By.XPATH, "//tr[3]/td[2]/div")
    AGE_50_AND_MORE = (By.XPATH, "//tr[4]/td[2]/div")

class ClientGenderLocators:
    TITLE_GENDER_OF_CLIENTS = (By.XPATH, "//p[contains(.,'Пол клиентов')]")
    PIE_CHART_GENDER_OF_CLIENTS = (By.ID, "genderData")
    GENDER_MALE = (By.XPATH, "//app-diagram-info-block[2]/div/div/app-table/table/tbody/tr/td[2]/div")
    GENDER_FEMALE = (By.XPATH, "//app-diagram-info-block[2]/div/div/app-table/table/tbody/tr[2]/td[2]/div")

class AverageClientsCheckLocators:
    TITLE_AVERAGE_CLIENTS_CHECK = (By.XPATH, "//p[contains(.,'Средний чек клиентов')]")
    PIE_CHART_AVERAGE_CLIENTS_CHECK = (By.ID, "averageCheckData")
    CHECK_UP_TO_300 = (By.XPATH, "//app-diagram-info-block[3]/div/div/app-table/table/tbody/tr/td[2]/div")
    CHECK_300_600 = (By.XPATH, "//app-diagram-info-block[3]/div/div/app-table/table/tbody/tr[2]/td[2]/div")
    CHECK_600_1000 = (By.XPATH, "//app-diagram-info-block[3]/div/div/app-table/table/tbody/tr[3]/td[2]/div")
    CHECK_1000_1500 = (By.XPATH, "//app-diagram-info-block[3]/div/div/app-table/table/tbody/tr[4]/td[2]/div")
    CHECK_1500_AND_MORE = (By.XPATH, "//tr[5]/td[2]/div")

class NumberOfPurchasesLocators:
    TITLE_NUMBER_OF_PURCHASES = (By.XPATH, "//p[contains(.,'Количество покупок')]")
    PIE_CHART_NUMBER_OF_PURCHASES = (By.ID, "numberOfPurchasesData")
    PURCHASE_1 = (By.XPATH, "//app-diagram-info-block[4]/div/div/app-table/table/tbody/tr/td[2]/div")
    PURCHASE_2 = (By.XPATH, "//app-diagram-info-block[4]/div/div/app-table/table/tbody/tr[2]/td[2]/div")
    PURCHASE_3 = (By.XPATH, "//app-diagram-info-block[4]/div/div/app-table/table/tbody/tr[3]/td[2]/div")
    PURCHASE_4 = (By.XPATH, "//app-diagram-info-block[4]/div/div/app-table/table/tbody/tr[4]/td[2]/div")
    PURCHASE_5_AND_MORE = (By.XPATH, "//app-diagram-info-block[4]/div/div/app-table/table/tbody/tr[5]/td[2]/div")

class TimeOfPurchaseLocators:
    TITLE_TIME_OF_PURCHASE = (By.XPATH, "//p[contains(.,'Время совершения покупок')]")
    PIE_CHART_TIME_OF_PURCHASE = (By.ID, "timeOfPurchasesData")
    TIME_0_9 = (By.XPATH, "//app-diagram-info-block[5]/div/div/app-table/table/tbody/tr/td[2]/div")
    TIME_9_11 = (By.XPATH, "//app-diagram-info-block[5]/div/div/app-table/table/tbody/tr[2]/td[2]/div")
    TIME_11_13 = (By.XPATH, "//app-diagram-info-block[5]/div/div/app-table/table/tbody/tr[3]/td[2]/div")
    TIME_13_15 = (By.XPATH, "//app-diagram-info-block[5]/div/div/app-table/table/tbody/tr[4]/td[2]/div")
    TIME_15_17 = (By.XPATH, "//app-diagram-info-block[5]/div/div/app-table/table/tbody/tr[5]/td[2]/div")
    TIME_17_19 = (By.XPATH, "//tr[6]/td[2]/div")
    TIME_19_24 = (By.XPATH, "//tr[7]/td[2]/div")

class DayOfPurchaseLocators:
    TITLE_DAY_OF_PURCHASE = (By.XPATH, "//p[contains(.,'Дни совершения покупок')]")
    PIE_CHART_DAY_OF_PURCHASE = (By.ID, "dayOfPurchasesData")
    MONDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr/td[2]/div")
    TUESDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[2]/td[2]/div")
    WEDNESDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[3]/td[2]/div")
    THURSDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[4]/td[2]/div")
    FRIDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[5]/td[2]/div")
    SATURDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[6]/td[2]/div")
    SUNDAY = (By.XPATH, "//app-diagram-info-block[6]/div/div/app-table/table/tbody/tr[7]/td[2]/div")