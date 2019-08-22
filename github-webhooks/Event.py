class Event:
    def __init__(self,data,event=None):
        assert type(data) is dict, "data is of type {} not dict".format(type(data))
        self.data = data

    def __getattr__(self, item):
        if item not in self.data:
            return False
        output = self.data[item]
        while type(output) is dict:
            output = Event(output)  # So nested attributes work - probably a better way to do this
        return output

    def __repr__(self):
        if type(self.data) is dict:
            return self.data
        else:
            return object.__repr__(self)

    def __str__(self):
        return str(self.__repr__())  # override to force string - repr can return dict