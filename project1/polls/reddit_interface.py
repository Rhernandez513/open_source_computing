import praw
import os

# https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth

try:
    reddit = praw.Reddit(client_id=os.environ['reddit_client_id'],
                         client_secret= os.environ['reddit_secret_token'],
                         redirect_uri='http://localhost:8080',
                         user_agent='test script')

    reddit_api = reddit.subreddit("all")
except:
    print('Failed to import Reddit Keys')
    reddit = None

# print(reddit.auth.url(['identity'], '...', 'permanent'))

# for i in all.search("yellow car", limit=5) :
    # print(i.title)
