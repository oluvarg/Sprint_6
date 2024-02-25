from selenium.webdriver.common.by import By


class OrderPageLocators:
    CONTENT_TITLE = By.XPATH, './/div[text()="Для кого самокат"]'

    NAME_REG_LOCATOR = By.XPATH, './/input[@placeholder = "* Имя"]'

    SECOND_NAME_REG_LOCATOR = By.XPATH, './/input[@placeholder = "* Фамилия"]'

    ADDRESS_REG_LOCATOR = By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'

    PHON_NUM_REG_LOCATOR = By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'

    LOGO_SCOOTER = By.XPATH, './/a[@href = "/"]'

    BUTTON_NEXT = By.XPATH, './/button[text()="Далее"]'

    COMBOBOX_METRO = By.XPATH, './/div[@class="select-search"]'

    BUTTON_METRO_1 = By.XPATH, './/button[@value="1"]'  # Бульвар Рокоссовского

    BUTTON_METRO_2 = By.XPATH, './/button[@value="2"]'  # Черкизовская

    DATE = By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]'

    BLACK_CHECKBOX = By.XPATH, './/label[@for = "black"]'

    GREY_CHECKBOX = By.XPATH, './/label[@for = "grey"]'

    TIME_COMBOBOX = By.XPATH, './/div[text() = "* Срок аренды"]'

    TWO_DAYS = By.XPATH, './/div[text()="двое суток"]'

    FOUR_DAYS = By.XPATH, './/div[text()="четверо суток"]'

    BUTTON_ORDER = By.XPATH, './/button[2][text() = "Заказать"]'  # /html/body/div/div/div[2]/div[3]/button[2]

    BUTTON_YES = By.XPATH, './/button[text() = "Да"]'

    CONFIRM = By.XPATH, './/div[text() = "Заказ оформлен"]'



