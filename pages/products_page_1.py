import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.loggers import Logger


class Products_page_1(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    filter_button = '//button[@data-link="{on showDesktopFiltres}"]'
    price_start = '//input[@name="startN"]'
    price_finish = '//input[@name="endN"]'
    brand_1 = '//span[contains(text(), "Apple")]'
    discount = '//span[contains(text(), "от 10% и выше")]'
    phone_memory_checkbox = '//div[13]/div/ul/li[2]/div'
    show_button = '//button[contains(@data-link, "applyFiltres")]'




    # Getters

    def get_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_price_start(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_start)))

    def get_price_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_finish)))

    def get_brand_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_1)))


    def get_discount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount)))

    def get_phone_memory_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_memory_checkbox)))


    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    # Actions

    def click_filter_button(self):
        self.get_filter_button().click()
        print('Click filter button')

    def input_price_start(self, price_start):
        self.get_price_start().clear()
        self.get_price_start().send_keys(price_start)
        print('Input price start')

    def input_price_finish(self, price_finish):
        self.get_price_finish().send_keys(Keys.BACKSPACE*7)
        self.get_price_finish().send_keys(price_finish)
        print('Input price finish')

    def choice_brand_1(self):
        self.get_brand_1().click()
        print('Choice brand 1')

    def choice_discount(self):
        self.get_discount().click()
        print('Choice discount')

    def choice_phone_memory(self):
        self.get_phone_memory_checkbox().click()
        print('Choice phone memory')

    def click_show_button(self):
        self.get_show_button().click()
        print('Click show button')

    # Methods

    def search_with_filters(self):
        Logger.add_start_step(method='search_with_filters')
        self.click_filter_button()
        time.sleep(1)
        self.input_price_start('10000')
        time.sleep(1)
        self.input_price_finish('50000')
        time.sleep(1)
        self.choice_brand_1()
        time.sleep(1)
        self.choice_discount()
        time.sleep(1)
        self.choice_phone_memory()
        time.sleep(1)
        self.click_show_button()
        Logger.add_end_step(url=self.driver.current_url, method='search_with_filters')
