
from os import environ

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
chromeOptions = ChromeOptions()
chromeOptions.add_argument('ignore-certificate-errors')
chromeOptions.headless = False

class BrowserDriverFactory(object):
    def __init__(self):
        self.driver = webdriver.Chrome(chromeOptions)
        self.driver.set_window_size(1920, 1080)

    def getBrowser(self):
        return self.driver
