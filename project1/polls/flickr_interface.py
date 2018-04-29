from flickrapi import FlickrAPI
import os

# https://github.com/alexis-mignon/python-flickr-api/tree/master/flickr_api

try:
    flickr = FlickrAPI(api_key = os.environ['flickr_api_key'],
                       api_secret = os.environ['flickr_api_secret'],
                       format='parsed-json')
except:
    print('Failed to import Flickr Keys')
    flickr = None

