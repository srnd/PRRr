class User:
    def __init__(self,data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self,attribute,data[attribute])

    def __str__(self):
        return self.login


class Issue:
    def __init__(self,data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self,attribute,data[attribute])
        # Override attributes containing nested json with proper classes
        self.user = User(self.user)


class Repository:
    def __init__(self, data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self, attribute, data[attribute])
        # Override attributes containing nested json with proper classes
        self.owner = User(self.owner)


class Comment:
    def __init__(self, data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self, attribute, data[attribute])
        # Override attributes containing nested json with proper classes
        self.user = User(self.user)