from behave.fixture import use_fixture
from test_helper.custom_logger import CustomLogger
from test_helper.browserDriverFactory import BrowserDriverFactory
from products_test import ProductsTest
import os

log =CustomLogger()
logger = log.custom_logger('INFO', os.path.abspath('./ui_test.log'))


def before_all(context):
    context.logger = logger
    context.timeout = 60

def before_feature(context, tag):
    browser_factory = BrowserDriverFactory()
    context.driver = browser_factory.getBrowser()

def after_feature(context, tag):
    context.driver.quit()

def before_scenario(context, scenario):
    context.products_test = ProductsTest(context)