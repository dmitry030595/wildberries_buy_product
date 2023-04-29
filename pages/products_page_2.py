import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.loggers import Logger


class Products_page_2(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product = '//a[@draggable="false"]'
    name_product = '//span[@class="product-card__name"]'
    price_product = '//ins[@class="price__lower-price"]'

    # Getters

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.price_product)))

    # Actions

    def get_name_of_product(self):
        name_product = self.get_name_product()
        name_product = name_product.text
        fw = open('doc/file_1.txt', 'w')
        fw.write(f'{name_product[2:]}')
        fw.close()
        print('Name of product: ' + name_product[2:])

    def get_price_of_product(self):
        price_product = self.get_price_product()
        price_product = price_product.text
        fw = open('doc/file_2.txt', 'w')
        fw.write(f'{price_product[:-2]}')
        fw.close()
        print('Price of product: ' + price_product)

    def click_product(self):
        self.get_product().click()
        print('Click product')

    # Methods

    def choice_product(self):
        Logger.add_start_step(method='choice_product')
        self.get_name_of_product()
        self.get_price_of_product()
        self.click_product()
        Logger.add_end_step(url=self.driver.current_url, method='choice_product')
