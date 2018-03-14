import praw
import os

# https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth

reddit = praw.Reddit(client_id=os.environ['reddit_client_id'],
                     client_secret= os.environ['reddit_secret_token'],
                     redirect_uri='http://localhost:8080',
                     user_agent='test script')
# print(reddit.auth.url(['identity'], '...', 'permanent'))

reddit_api = reddit.subreddit("all")
# for i in all.search("yellow car", limit=5) :
    # print(i.title)
