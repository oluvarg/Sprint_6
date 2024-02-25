from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'

    ANSWER_LOCATOR = By.XPATH, './/div[@aria-labelledby="accordion__heading-{}"]'

    QUESTION_LOCATOR_FIRST = By.XPATH, './/div[@id="accordion__heading-0"]'

    BUTTON_ORDER_FIRST = By.XPATH, './/div[2]/button[text() = "Заказать"]'

    BUTTON_ORDER_LAST = By.XPATH, './/div[5]/button[text() = "Заказать"]'

    LOGO_YANDEX = By.XPATH, './/a[@href="//yandex.ru"]'

    CLOSE_WINDOW_DZEN = By.XPATH, './/span[@tabindex = "0"]'
