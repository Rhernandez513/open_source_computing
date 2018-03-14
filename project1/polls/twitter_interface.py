import twitter
import os

# https://github.com/bear/python-twitter/wiki

tweet_api = twitter.Api(consumer_key = os.environ['twitter_consumer_key'],
		  consumer_secret = os.environ['twitter_consumer_secret'],
		  access_token_key = os.environ['twitter_access_token'],
		  access_token_secret = os.environ['twitter_access_token_secret'])

# print(api.VerifyCredentials())

# print(api.GetSearch("Hello World"))
