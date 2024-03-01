import allure

from pages.main_page import MainPage


class TestRedirects:

    @allure.title('Проверка перехода на страницу "Дзен" с помощью логотоипа "Яндекс"')
    def test_jump_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url_main()
        ya_url = main_page.jump_dzen_and_get_url()

        assert 'dzen.ru' in ya_url, 'Не удалось перейти на страницу Дзен'
