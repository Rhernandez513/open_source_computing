import twitter
import os

# https://github.com/bear/python-twitter/wiki

try:
    tweet_api = twitter.Api(consumer_key = os.environ['twitter_consumer_key'],
		  consumer_secret = os.environ['twitter_consumer_secret'],
		  access_token_key = os.environ['twitter_access_token'],
		  access_token_secret = os.environ['twitter_access_token_secret'])
except:
    print('Failed to import Twitter Keys')
    tweet_api = twitter.Api()

# print(api.VerifyCredentials())

# print(api.GetSearch("Hello World"))
