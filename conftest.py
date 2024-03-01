import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=firefox_options)
    yield driver
    driver.quit()
