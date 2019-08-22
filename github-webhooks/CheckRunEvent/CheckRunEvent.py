from .. import Event


class CheckRunEvent(Event):
    def __init__(self,data):
        super().__init__(data)