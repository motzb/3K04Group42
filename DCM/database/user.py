# A utility class for User
class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def get_list(self):
        return [self.username, self.password]


