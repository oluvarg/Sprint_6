
import pytest

from data import DataAnswer, DataTitle
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'q_num,a_num,expected_result',
        [
            (0, 0, DataAnswer.ANSWER_Q_0),
            (1, 1, DataAnswer.ANSWER_Q_1),
            (2, 2, DataAnswer.ANSWER_Q_2),
            (3, 3, DataAnswer.ANSWER_Q_3),
            (4, 4, DataAnswer.ANSWER_Q_4),
            (5, 5, DataAnswer.ANSWER_Q_5),
            (6, 6, DataAnswer.ANSWER_Q_6),
            (7, 7, DataAnswer.ANSWER_Q_7),
        ]
    )
    def test__question_and_get_answer(self, driver, q_num, a_num, expected_result):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        main_page = MainPage(driver)

        method_q, locator_q = MainPageLocators.QUESTION_LOCATOR
        locator_q = locator_q.format(q_num)

        method_a, locator_a = MainPageLocators.ANSWER_LOCATOR
        locator_a = locator_a.format(a_num)

        result = main_page.click_to_question_and_get_answer_text(
            (method_q, locator_q),
            (method_a, locator_a))

        assert main_page.check_answer(result, expected_result), 'Текст ответа не соответствует ожидаемому'

    @pytest.mark.parametrize(
        "locators",
        [MainPageLocators.BUTTON_ORDER_FIRST,
         MainPageLocators.BUTTON_ORDER_LAST]
    )
    def test_order_button(self, driver, locators):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.scroll_to_order_and_click(locators)
        result = main_page.get_text_from_element(OrderPageLocators.CONTENT_TITLE)
        expected_result = DataTitle.TITLE_ORDER

        assert (result, expected_result), 'Не удалось перейти на страницу заказа'

    def test_jump_dzen(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        ya_url = main_page.jump_dzen_and_get_url(MainPageLocators.LOGO_YANDEX)

        assert 'dzen.ru' in ya_url, 'Не удалось перейти на страницу Дзен'
