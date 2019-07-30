class User:
    def __init__(self,data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self,attribute,data[attribute])

    def __repr__(self):
        return self.login

    def __str__(self):
        return self.login