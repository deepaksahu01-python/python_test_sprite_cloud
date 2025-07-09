from test_helper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ShoppingCartPage(SeleniumDriver):
    cart_icon = '//*[@id="shopping_cart_container"]'
    your_cart = "//*[contains(text(), 'Your Cart')]"
    inventory_items = '//*[@class="inventory_item_name"]'

    def __init__(self, context):
        super(ShoppingCartPage, self).__init__(context)
        self.driver = context.driver

    def click_cart_icon(self):
        self.element_click(self.cart_icon)

    def get_inventory_items(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.your_cart)))   
        return self.get_elements(self.inventory_items, 'xpath')

    