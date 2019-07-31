from webhooks.events import Event, IssueComment


def receive_hook(request):
    #  TODO: Double check signature, that it is from github, is valid, etc.
    print(request.headers)
    if request.headers['X-Github-Event'] == 'issue_comment':
        return IssueComment(request)
    return Event(request)