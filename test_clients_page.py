from base_page import BasePage
from clients import Clients
from auth import Auth
from pie_charts.clients_ages import ClientsAges
from pie_charts.clients_gender import ClientGender
from pie_charts.average_clients_check import AverageClientsCheck
from pie_charts.number_of_purchases import NumberOfPurchases
from pie_charts.time_of_purchase import TimeOfPurchase
from pie_charts.day_of_purchase import DayOfPurchase

def test_age_of_clients(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Возраст клиентов"
    clients_age = ClientsAges(browser, clients_page)
    clients_age.title_ages_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    clients_age.pie_chart_ages_presented()
    # Проверить возрастные диапазоны
    # 14 - 24
    clients_age.age_ranges_14_24()
    # 25 - 35
    clients_age.age_ranges_25_35()
    # 36 - 49
    clients_age.age_ranges_36_49()
    # 50 and more
    clients_age.age_ranges_50_and_more()

def test_gender_of_clients(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Пол клиентов"
    clients_gender = ClientGender(browser, clients_page)
    clients_gender.title_gender_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    clients_gender.pie_chart_gender_presented()
    # Проверить пол
    # Мужской
    clients_gender.gender_male()
    # Женский
    clients_gender.gender_female()

def test_average_clients_check(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Средний чек клиентов"
    average_clients_check= AverageClientsCheck(browser, clients_page)
    average_clients_check.title_average_clients_check_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    average_clients_check.pie_chart_average_clients_check_presented()
    # Проверить средний чек
    # до 300
    average_clients_check.check_up_to_300()
    # 300-600
    average_clients_check.check_300_600()
    # 600-100
    average_clients_check.check_600_1000()
    # 1000-1500
    average_clients_check.check_1000_1500()
    # 1500 и больше
    average_clients_check.check_1500_and_more()

def test_number_of_purchases(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Количество покупок"
    number_of_purchases = NumberOfPurchases(browser, clients_page)
    number_of_purchases.title_number_of_purchases_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    number_of_purchases.pie_chart_number_of_purchases_presented()
    # Проверить кол-во покупок
    # 1 покупка
    number_of_purchases.purchase_1()
    # 2 покупки
    number_of_purchases.purchase_2()
    # 3 покупки
    number_of_purchases.purchase_3()
    # 4 покупки
    number_of_purchases.purchase_4()
    # 5 и более покупок
    number_of_purchases.purchase_5_and_more()

def test_time_of_purchase(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Время совершения покупок"
    time_of_purchase = TimeOfPurchase(browser, clients_page)
    time_of_purchase.title_time_of_purchase_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    time_of_purchase.pie_chart_time_of_purchase_presented()
    # Проверить временные интервалы
    # 0-9 часов
    time_of_purchase.time_0_9()
    # 9-11 часов
    time_of_purchase.time_9_11()
    # 11-13 часов
    time_of_purchase.time_11_13()
    # 13-15 часов
    time_of_purchase.time_13_15()
    # 15-17 часов
    time_of_purchase.time_15_17()
    # 17-19 часов
    time_of_purchase.time_17_19()
    # 19-24 часов
    time_of_purchase.time_19_24()

def test_day_of_purchase(browser):
    link = ""
    clients_page = ""
    # Партнер авторизовался в ЛК портала для партнеров
    page = Auth(browser, link)
    page.successful_auth()
    # Партнер перещел к разделу с аналитикой по клиентам "Клиенты"
    clients_page = Clients(browser, link)
    clients_page.go_to_clients()
    # На странице ищем раздел "Время совершения покупок"
    day_of_purchase = DayOfPurchase(browser, clients_page)
    day_of_purchase.title_day_of_purchase_presented()
    # Партнеру в ЛК на странице "Клиенты" отображается соответствующий pie chart
    day_of_purchase.pie_chart_day_of_purchase_presented()
    # Проверить дни недели
    # Понедельник
    day_of_purchase.monday()
    # Вторник
    day_of_purchase.tuesday()
    # Среда
    day_of_purchase.wednesday()
    # Четверг
    day_of_purchase.thursday()
    # Пятница
    day_of_purchase.friday()
    # Суббота
    day_of_purchase.saturday()
    # Воскресенье
    day_of_purchase.sunday()
