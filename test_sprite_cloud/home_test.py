from page_objects.home_page import HomePage

class HomeTest:
    '''
    Contains methods and varaibles to perform actions on login page
    '''
    item_name_to_locator_substring = {
        'Bolt T-Shirt': 'bolt-t-shirt'
    }

    def __init__(self, context):
        self.context = context
        self.home_page = HomePage(context)

    def add_item_to_cart(self, item):
        item_name = self.item_name_to_locator_substring[item].lower()
        self.home_page.click_add_to_cart(item_name)
