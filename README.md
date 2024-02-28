# Sprint_6

## Описание 
### В данном проекте написаны тесты для сайта https://qa-scooter.praktikum-services.ru/. Использован POM и параметризация.

## Содержимое проекта:

 * `allure_results` - сожержит отчеты alure
 *  `locators` - дирректория локаторов
 * * `main_page_locators.py` - локаторы для главной страницы 
 * * `order_page_locators.py` - локаторы для страницы заказа
 * `pages` - дирректория методов страниц
 * * `base_page.py` - общие методы
 * * `main_page.py` - методы для главной страницы
 * * `order_page.py` - методы для страницы заказа 
 * `tests` - тесты
 * * `test_main_page.py` - тесты для главной страницы
 * * `test_order_page.py` - тесты для страницы заказа
 * `conftest.py` -  фикстуры
 * `date.py` - данные для параметризации
 * `README.md`

## Запуск тестов:

* `pytest .\tests\test_main_page.py, .\tests\test_order_page.py --alluredir=allure_results` - Запуск и получение allure отчета

* `allure serve allure_results` - отображение полученных отчетов