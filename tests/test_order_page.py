import allure
import pytest

from data import DataOrderForm
from locators.order_page_locators import OrderPageLocators

from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
        'name,'
        'second_name,'
        'address,'
        'locator_station,'
        'date,'
        'color_locator,'
        'time_locator',
        [
            (DataOrderForm.name_1,
             DataOrderForm.second_name_1,
             DataOrderForm.address_1,
             OrderPageLocators.BUTTON_METRO_1,
             DataOrderForm.date_1,
             OrderPageLocators.BLACK_CHECKBOX,
             OrderPageLocators.TWO_DAYS
             ),
            (DataOrderForm.name_2,
             DataOrderForm.second_name_2,
             DataOrderForm.address_2,
             OrderPageLocators.BUTTON_METRO_1,
             DataOrderForm.date_2,
             OrderPageLocators.GREY_CHECKBOX,
             OrderPageLocators.FOUR_DAYS
             )
        ],

    )
    def test_order_form(self, driver, name, second_name, address, locator_station, date, color_locator,
                        time_locator):
        order_page = OrderPage(driver)
        order_page.go_to_url_order()
        number = DataOrderForm.number_phone
        order_page.set_text_to_first_form(OrderPageLocators.NAME_REG_LOCATOR, name,
                                          OrderPageLocators.SECOND_NAME_REG_LOCATOR, second_name,
                                          OrderPageLocators.ADDRESS_REG_LOCATOR, address,
                                          OrderPageLocators.PHON_NUM_REG_LOCATOR, number
                                          )
        order_page.choice_metro(OrderPageLocators.COMBOBOX_METRO, locator_station)
        order_page.click_on_element(OrderPageLocators.BUTTON_NEXT)

        order_page.set_text_to_second_form(OrderPageLocators.DATE, date)
        order_page.click_on_element(color_locator)
        order_page.choice_time(OrderPageLocators.TIME_COMBOBOX, time_locator)
        result = order_page.click_on_order_and_get_text_notification(OrderPageLocators.BUTTON_ORDER,
                                                                     OrderPageLocators.BUTTON_YES,
                                                                     OrderPageLocators.CONFIRM)

        assert 'Заказ оформлен' and 'Номер заказа:' in result, 'Не удалось оформить заказ'

    @allure.title('Проверка перехода на главную страницу')
    def test_jump_main_paige(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_url_order()
        result = order_page.jump_main_page_from_order_and_get_content()
        assert "Сколько это стоит?" in result
