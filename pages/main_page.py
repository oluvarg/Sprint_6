
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_to_question_and_get_answer_text(self, locator_q, locator_a):
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    def check_answer(self, result, expected_result):
        return result == expected_result

    def scroll_to_order_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    def get_text_from_order_title(self, locator):
        return self.get_text_from_element(locator)

    def check_jump_order_page(self, result, expected_result):
        return result == expected_result

    def jump_dzen_and_get_url(self, logo_locator):
        self.click_on_element(logo_locator)
        self.driver.switch_to.window(self.driver.window_handles[1])
        if self.find_element_with_wait(MainPageLocators.CLOSE_WINDOW_DZEN):
            self.click_on_element(MainPageLocators.CLOSE_WINDOW_DZEN)
        ya_url = self.driver.current_url
        return ya_url


