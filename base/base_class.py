import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%H')
        now_date_1 = int(now_date) + 6
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.' + str(now_date_1) + '.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Дмитрий\\PycharmProjects\\wildberries_buy_product'
                                    '\\screen\\' + name_screenshot)
        print('Screenshot done')

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
