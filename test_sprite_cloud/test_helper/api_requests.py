import requests


class ApiRequests:
    """
    This class contains variables and methods to generate/create/receive api requests
    """
    # Additional headers.
    headers = {'Content-Type': 'application/json' }

    def __init__(self, logger=None):
        self.logger = logger

    def get_response(self, request_url, payload=[]):
        response = requests.get(request_url, data=payload)
        self.logger.critical('Response code:{} and response payload:{}'.format(response.status_code, response.json()))
        return response

    def post_response(self, request_url, payload=[]):
        response = requests.post(request_url, data=payload)
        self.logger.critical('Response code:{} and response payload:{}'.format(response.status_code, response.json()))
        return response



