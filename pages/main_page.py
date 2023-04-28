import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    search = '//input[@id="searchInput"]'

    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    # Actions

    def input_product_in_search(self, product_name):
        self.get_search().send_keys(product_name)
        print('Input product in search')


    # Methods

    def search_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(5)
        self.input_product_in_search('Смартфоны')
        self.get_search().send_keys(Keys.RETURN)
        self.assert_url('https://www.wildberries.ru/catalog/0/'
                        'search.aspx?search=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B')
