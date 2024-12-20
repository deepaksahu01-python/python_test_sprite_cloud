from test_helper.custom_logger import CustomLogger
import os
from user_management_test import UserManagementTest



log =CustomLogger()
logger = log.custom_logger('INFO', os.path.abspath('./api_test.log'))


def before_all(context):
    context.logger = logger

def before_feature(context, tag):
    pass

def after_feature(context, tag):
    pass

def before_scenario(context, scenario):
    context.user_management_test = UserManagementTest(context)