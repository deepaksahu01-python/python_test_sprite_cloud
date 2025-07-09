from test_helper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(SeleniumDriver):
    # locators
    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    login_button = '//*[@id="login-button"]'
    locked_user_msg = '//*[@class="error-message-container error"]'

    def __init__(self, context):
        super(LoginPage, self).__init__(context)
        self.driver = context.driver

    def enter_username(self, user_name):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.user_name)))
        self.sendKeys(user_name, self.user_name)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.password)))
        self.sendKeys(password, self.password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
        self.element_click(self.login_button)

    def get_locked_user_msg(self):
        login_error_msg = self.get_element(self.locked_user_msg).text
        return login_error_msg