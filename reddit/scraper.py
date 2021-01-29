import praw

# New Scraper
def getnew(wsb: praw.reddit.models.Subreddit, limit=10, update=False):
    pass

# Top Hot
def gethot(wsb: praw.reddit.models.Subreddit, limit=10, update=False):
    pass

# Comment Scraper
def getcomments(wsb: praw.reddit.models.Subreddit, id, limit=10, update=False):
    pass

# Top Past X
def getpast(wsb: praw.reddit.models.Subreddit, time='week', limit=10, update=False):
    if time == 'hour':
        pass
    elif time == 'day':
        pass
    elif time == 'week':
        pass
    elif time == 'month':
        pass
    elif time == 'year':
        pass
    elif time == 'all':
        pass
    else:
        pass

