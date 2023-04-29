import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.products_page_2 import Products_page_2
from utilites.loggers import Logger


class Products_page_3(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver






    # Locators

    name_product = '//h1[@data-link="text{:selectedNomenclature^goodsName}"]'
    price_product = '//*[@class="product-page"]/div[3]/div[9]/div/div[1]/div[1]/div/div/p/span/ins'
    add_cart = '//*[@class="product-page"]/div[3]/div[9]/div/div[1]/div[2]/div/button[2]'
    cart = '//span[@class="navbar-pc__icon navbar-pc__icon--basket"]'

    # Getters

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.add_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.cart)))

    # Actions

    def get_name_of_product(self):
        name_product = self.get_name_product()
        name_product = name_product.text
        fr = open('doc/file_1.txt', 'r')
        text = fr.read()
        fr.close()
        print('Name of product: ' + name_product)
        assert name_product == text

    def get_price_of_product(self):
        price_product = self.get_price_product()
        price_product = price_product.text
        fr = open('doc/file_2.txt', 'r')
        text = fr.read()
        fr.close()
        print('Price of product: ' + price_product)
        assert price_product[:-2] == text

    def add_to_cart(self):
        self.get_add_cart().click()
        print('Add product to cart')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    # Methods

    def add_to_cart_and_click(self):
        Logger.add_start_step(method='add_to_cart_and_click')
        time.sleep(3)
        self.get_name_of_product()
        self.get_price_of_product()
        self.add_to_cart()
        time.sleep(2)
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_and_click')

