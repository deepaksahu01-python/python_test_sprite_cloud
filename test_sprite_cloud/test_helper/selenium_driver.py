from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver(object):

    def __init__(self, context):
        self.driver = context.driver
        self.wait = WebDriverWait(self.driver, context.timeout)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            return False

    def get_element(self, locator, locatorType="xpath"):
        element = None
        byType = self.getByType(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    def get_elements(self, locator, locatorType="xpath"):
        element = None
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.driver.find_elements(byType, locator)
        return element

    def element_click(self, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        element.click()

    def sendKeys(self, data, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        element.send_keys(data)

