import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.products_page_2 import Products_page_2
from utilites.loggers import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    name_product = '//span[@class="good-info__good-name"]'
    price_product = '//p[@class="b-top__total line"]//span[contains(@data-link, "Money")]'
    button_choice_user_address = '//div[@data-link="{on showDeliveryPopup}"]'  # Кнопка выбрать адрес доставки
    user_address = '//input[@placeholder="Введите адрес"]'  # Поле ввода адреса
    button_search = '//ymaps[contains(text(), "Найти")]'  # Кнопка "Найти" (адрес)
    find_user_address = '//div[@class="address-item__name"]'  # Найденный адрес
    value_user_address1 = '//span[@class="details-self__name-text"]'  # Полный адрес из поиска
    button_choice_address = '//button[@class="details-self__btn btn-main"]'  # Кнопка выбора адреса
    value_user_address2 = '//*[@id="basketForm"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div/span[1]'  # Полный адрес из страницы заказа
    button_order = '//button[@name="ConfirmOrderByRegisteredUser"]'

    # Getters

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_button_choice_user_address(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
            By.XPATH, self.button_choice_user_address)))

    def get_user_address(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.user_address)))

    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search)))

    def get_find_user_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.find_user_address)))

    def get_value_user_address1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_user_address1)))

    def get_button_choice_address(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
            By.XPATH, self.button_choice_address)))

    def get_value_user_address2(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
            By.XPATH, self.value_user_address2)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

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

    def click_button_choice_user_address(self):
        self.get_button_choice_user_address().click()
        print('Click button choice user address')

    def input_user_address(self):
        self.get_user_address().send_keys('Костанайская область, Рудный, улица Павла Корчагина, 108')
        print('Click cart')

    def click_button_search(self):
        self.get_button_search().click()
        print('Click button search')

    def click_find_user_address(self):
        self.get_find_user_address().click()
        print('Click find user address')

    def write_value_user_address1(self):
        value_user_address1 = self.get_value_user_address1().text
        fw = open('doc/file_3.txt', 'w')
        fw.write(f'{value_user_address1}')
        fw.close()
        print('Value user address1: ' + value_user_address1)

    def click_button_choice_address(self):
        self.get_button_choice_address().click()
        print('Click button choice address')

    def assert_value_user_address2(self):
        value_user_address2 = self.get_value_user_address2().text
        fr = open('doc/file_3.txt', 'r')
        text = fr.read()
        fr.close()
        print('Value user address2: ' + value_user_address2[:-1])
        assert text == value_user_address2[:-1]

    def click_button_order(self):
        self.get_button_order().click()
        print('Click button order')

    # Methods

    def order_product(self):
        Logger.add_start_step(method='order_product')
        time.sleep(3)
        self.get_name_of_product()
        self.get_price_of_product()
        self.click_button_choice_user_address()
        self.input_user_address()
        self.click_button_search()
        time.sleep(2)
        self.click_find_user_address()
        time.sleep(2)
        self.write_value_user_address1()
        self.click_button_choice_address()
        self.assert_value_user_address2()
        self.click_button_order()
        time.sleep(3)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='order_product')

