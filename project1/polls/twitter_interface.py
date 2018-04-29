import twitter
import os
from . import secret

# https://github.com/bear/python-twitter/wiki

c_key = secret.keys['twitter_consumer_key']
c_secret = secret.keys['twitter_consumer_secret']
a_t_key = secret.keys['twitter_access_token']
a_t_secret = secret.keys['twitter_access_token_secret']

if c_key != '' and c_secret != '' and a_t_key != '' and a_t_secret != '':
    try:
        tweet_api = twitter.Api(consumer_key = c_key,
                      consumer_secret = c_secret,
                      access_token_key = a_t_key,
                      access_token_secret = a_t_secret)
    except:
        print('Failed to import Twitter Keys')
        tweet_api = twitter.Api()
else:
    print('One or more Twitter Key values have not been entered in secret.py')
    tweet_api = twitter.Api()

# print(api.VerifyCredentials())

# print(api.GetSearch("Hello World"))
