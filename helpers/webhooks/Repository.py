from .User import User


class Repository:
    def __init__(self,data):
        for attribute in data:  # Set attribute for each item in json
            setattr(self,attribute,data[attribute])
        # Override attributes containing nested json with proper classes
        self.owner = User(self.owner)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name