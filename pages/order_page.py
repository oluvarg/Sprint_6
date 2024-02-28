import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Переход на страницу оформления заказа')
    def get_url_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

    @allure.step('Ввод данных в поля "Имя, Фамилия, Адрес, Номер телефона"')
    def set_text_to_first_form(self, nam_locator, name,
                               se_na_locator, second_name,
                               add_locator, address,
                               num_locator, number):
        self.set_text_to_element(nam_locator, name)
        self.set_text_to_element(se_na_locator, second_name)
        self.set_text_to_element(add_locator, address)
        self.set_text_to_element(num_locator, number)

    @allure.step('Открытие комбобокса "Метро" и выбор станции')
    def choice_metro(self, locator_combobox, locator_station):
        self.click_on_element(locator_combobox)
        self.click_on_element(locator_station)

    @allure.step('Ввод даты')
    def set_text_to_second_form(self, date_locator, date):
        self.set_text_to_element(date_locator, date)

    @allure.step('Выбор цвета')
    def choice_color(self, color_locator):
        self.click_on_element(color_locator)

    @allure.step('Выбор времени')
    def choice_time(self, combox_locator, time_locator):
        self.click_on_element(combox_locator)
        self.click_on_element(time_locator)

    @allure.step('Нажатие на кнопку "Заказать", "Да" и получение текста с окна поддверждения')
    def click_on_order_and_get_text_notification(self, order_locator, button_yes_locator, confirm_locator):
        self.click_on_element(order_locator)
        self.click_on_element(button_yes_locator)
        return self.get_text_from_element(confirm_locator)

    @allure.step('Нажатие на логотипа "Самокат" и получение текста первого вопроса')
    def jump_main_page_from_order(self, locator):
        self.click_on_element(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        return self.get_text_from_element(MainPageLocators.QUESTION_LOCATOR_FIRST)
