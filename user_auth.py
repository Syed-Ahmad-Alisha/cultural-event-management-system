class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Try a different one.")
        else:
            self.users[username] = password
            print("Registration successful!")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False
