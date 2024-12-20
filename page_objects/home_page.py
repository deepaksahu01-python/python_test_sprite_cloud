from test_helper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(SeleniumDriver):
    add_to_cart = '//*[@id="add-to-cart-sauce-labs-{}"]'
    url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, context):
        super(HomePage, self).__init__(context)
        self.driver = context.driver

    def click_add_to_cart(self, item):
        self.element_click(self.add_to_cart.format(item))

    