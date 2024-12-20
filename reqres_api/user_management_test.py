from test_helper.api_requests import ApiRequests
from test_helper.api_urls import ApiUrls

class UserManagementTest:

    def __init__(self, context):
        self.api_url = ApiUrls()
        self.api_requests = ApiRequests(context.logger)

    def get_user(self, id):
        single_user_url = '{}/{}'.format(self.api_url.single_user, id)
        return self.api_requests.get_response(single_user_url)

    def get_users(self):
        list_users_url = '{}{}'.format(self.api_url.list_users)
        return self.api_requests.get_response(list_users_url)

    def verify_user(self, actual_user, expected_user):
        for user_attribute in expected_user:
            actual_value = actual_user[user_attribute]
            expected_value = expected_user[user_attribute]
            assert actual_value == expected_value, 'The response was not good'

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        create_user_url = self.api_url.single_user
        return self.api_requests.post_response(create_user_url, payload)

    def verify_created_user(self, created_user, expected_user):
        actual_user = created_user.json()
        assert created_user.status_code == 201, 'The response was not good'
        self.verify_user(actual_user, expected_user)

    def verify_existing_user(self, existing_user, expected_user):
        actual_user = existing_user.json()['data']
        assert existing_user.status_code == 200, 'The response was not good'
        self.verify_user(actual_user, expected_user)

    def login(self, user_name):
        payload = {'email': user_name}
        return self.api_requests.post_response(self.api_url.login_url, payload)

    def verify_login(self, login_response, error_msg):
        actual_msg = login_response.json()['error']
        assert login_response.status_code == 400 and actual_msg == error_msg


        


