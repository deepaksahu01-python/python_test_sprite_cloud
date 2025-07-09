import logging
class CustomLogger(object):

    def custom_logger(self, log_level, file_name):
        logging.basicConfig(level=log_level, filename=file_name, filemode='a',
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger('')
        return logger