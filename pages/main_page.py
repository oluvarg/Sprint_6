import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Переход на главную страницу сайта')
    def get_url_main(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Скролл в конец страницы')
    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Нажиматие на вопрос и получение ответа')
    def click_to_question_and_get_answer_text(self, locator_q, locator_a):
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    @allure.step('Сравнение полученного ответа с ожидаемым')
    def check_answer(self, result, expected_result):
        return result == expected_result

    @allure.step('Скролл до кнопки "Заказать" и нажатие по кнопки "Заказать"')
    def scroll_to_order_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Получение текста из загаловка формы создания заказа')
    def get_content_title(self):
        return self.get_text_from_element(OrderPageLocators.CONTENT_TITLE)

    @allure.step('Нажатие на логотип "Яндекс" и получение url')
    def jump_dzen_and_get_url(self, logo_locator):
        self.click_on_element(logo_locator)
        self.jump_new_tab()
        if self.find_element_with_wait(MainPageLocators.CLOSE_WINDOW_DZEN):
            self.click_on_element(MainPageLocators.CLOSE_WINDOW_DZEN)
        ya_url = self.driver.current_url
        return ya_url
