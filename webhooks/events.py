import json
from models import Issue, Comment, Repository, User


class Event():
    def __init__(self,request):
        self.headers = request.headers
        data = json.loads(request.data)
        for attribute in data:  # Set attribute for each item in json
            setattr(self,attribute,data[attribute])


class IssueComment(Event):
    def __init__(self,request):
        super().__init__(request)
        self.issue = Issue(self.issue)
        self.comment = Comment(self.comment)
        self.repository = Repository(self.repository)
        self.sender = User(self.sender)

    def __str__(self):
        if self.action == 'created':
            return '''{comment.user} commented on issue #{issue.number} ({issue.title}):
"{comment.body}"'''.format(**vars(self))
