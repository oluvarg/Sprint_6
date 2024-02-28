import allure
import pytest

from data import DataAnswer, DataTitle
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка открытия вопроса и сравнение ожидаемого ответа с полученным')
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
        main_page = MainPage(driver)
        main_page.get_url_main()
        main_page.scroll_down_page()

        method_q, locator_q = MainPageLocators.QUESTION_LOCATOR
        locator_q = locator_q.format(q_num)

        method_a, locator_a = MainPageLocators.ANSWER_LOCATOR
        locator_a = locator_a.format(a_num)

        result = main_page.click_to_question_and_get_answer_text(
            (method_q, locator_q),
            (method_a, locator_a))

        assert main_page.check_answer(result, expected_result), 'Текст ответа не соответствует ожидаемому'

    @allure.title('Проверка перехода на страницу оформления заказа')
    @pytest.mark.parametrize(
        "order_locators",
        [MainPageLocators.BUTTON_ORDER_FIRST,
         MainPageLocators.BUTTON_ORDER_LAST]
    )
    def test_order_button(self, driver, order_locators):
        main_page = MainPage(driver)
        main_page.get_url_main()
        main_page.scroll_to_order_and_click(order_locators)
        result = main_page.get_content_title()
        expected_result = DataTitle.TITLE_ORDER

        assert result == expected_result, 'Не удалось перейти на страницу оформления заказа'


class TestGoURL:

    @allure.title('Проверка перехода на страницу "Дзен" с помощью логотоипа "Яндекс"')
    def test_jump_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.get_url_main()
        ya_url = main_page.jump_dzen_and_get_url(MainPageLocators.LOGO_YANDEX)

        assert 'dzen.ru' in ya_url, 'Не удалось перейти на страницу Дзен'
