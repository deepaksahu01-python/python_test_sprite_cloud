from login_test import LoginTest
from home_test import HomeTest
from shopping_cart_test import ShoppingCartTest

class ProductsTest:

    def __init__(self, context):
        self.driver = context.driver
        self.login_test = LoginTest(context)
        self.home_test = HomeTest(context)
        self.shopping_cart_test = ShoppingCartTest(context)

    def login(self, url, user_name, password):
        self.driver.get(url)
        if self.driver.current_url == url:
            self.login_test.login(user_name, password)

    
    def add_item_to_cart(self, item):
        self.home_test.add_item_to_cart(item)

    def verify_item_at_checkout(self, item):
        self.shopping_cart_test.verify_item(item)

    def verify_logging(self):
        self.login_test.verify_logging()


