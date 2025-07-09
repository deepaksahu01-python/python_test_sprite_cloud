class ApiUrls:
    base_url = 'https://reqres.in/api/'

    def __init__(self):
        self.list_users = '{}users?page=2'.format(self.base_url)
        self.single_user = '{}users'.format(self.base_url)
        self.login_url = '{}login'.format(self.base_url)
