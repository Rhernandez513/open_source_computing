import praw
import os
from . import secret

# https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth

red_id=secret.keys['reddit_client_id']
red_secret= secret.keys['reddit_secret_token']

if red_id != '' and red_secret != '' :
    try:
        reddit = praw.Reddit(client_id=red_id,
                             client_secret=red_secret,
                             redirect_uri='http://localhost:8080',
                             user_agent='test script')

        reddit_api = reddit.subreddit("all")
    except:
        print('Failed to import Reddit Keys')
else:
    print('One or more Reddit Key values have not been entered in secret.py')

# print(reddit.auth.url(['identity'], '...', 'permanent'))

# for i in all.search("yellow car", limit=5) :
    # print(i.title)
