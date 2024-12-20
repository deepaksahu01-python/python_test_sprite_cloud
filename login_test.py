from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage

class LoginTest:
    '''
    Contains methods and varaibles to perform actions on login page
    '''

    def __init__(self, context):
        self.context = context
        self.login_page = LoginPage(context)
        self.home_page = HomePage(context)

    def login(self, user_name, password):
        self.login_page.enter_username(user_name)
        self.login_page.enter_password(password)
        self.login_page.click_login()

    def verify_logging(self):
        if self.context.driver.current_url == self.home_page.url:
            assert True, 'User was logged in'
        else:
            login_error_msg = self.login_page.get_locked_user_msg()
            self.context.logger.error(login_error_msg)
            assert False, 'User was not logged in'
            