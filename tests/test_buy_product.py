import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.products_page_1 import Products_page_1
from pages.products_page_2 import Products_page_2
from pages.products_page_3 import Products_page_3

def test_buy_product(set_up):
    count = 1
    while count <= 3:
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument('--ignore-ssl-errors')
            g = Service('C:\\Users\\Дмитрий\\PycharmProjects\\resource\\chromedriver.exe')
            driver = webdriver.Chrome(options=options, service=g)

            print('Test №: ' + str(count))
            m = Main_page(driver)
            m.search_product()

            pp1 = Products_page_1(driver)
            time.sleep(3)
            pp1.search_with_filters()

            pp2 = Products_page_2(driver)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 350);")
            pp2.choice_product()

            pp3 = Products_page_3(driver)
            pp3.add_to_cart_and_click()

            cp = Cart_page(driver)
            cp.order_product()

            time.sleep(3)
            driver.close()
            break
        except TimeoutException:
            count += 1
            driver.close()
            print("TimeoutException")

# python -m pytest -s -v
# exceptions.TimeoutException