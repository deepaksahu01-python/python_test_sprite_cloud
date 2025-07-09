from page_objects.shopping_cart_page import ShoppingCartPage

class ShoppingCartTest:
    '''
    Contains methods and varaibles to perform actions on Shopping Cart page
    '''
    
    def __init__(self, context):
        self.context = context
        self.shopping_cart_page = ShoppingCartPage(context)



    def verify_item(self, item):
        self.shopping_cart_page.click_cart_icon()
        inventory_items = self.shopping_cart_page.get_inventory_items()
        self.context.logger.info("No.of inventory items at shopping cart: {}".format(len(inventory_items)))
        self.context.logger.info("Inventor item: {}".format(inventory_items[0].text))
        assert inventory_items[0].text == 'Sauce Labs {}'.format(item)
        assert  len(inventory_items) == 1
        