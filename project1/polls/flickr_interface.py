from flickrapi import FlickrAPI
from . import secret
import os

# https://github.com/alexis-mignon/python-flickr-api/tree/master/flickr_api

api_key = secret.keys['flickr_api_key']
api_secret = secret.keys['flickr_api_secret']


if api_key != '' and api_secret != '':
    try:
        flickr = FlickrAPI(api_key,
                           api_secret,
                           format='parsed-json')
    except:
        print('Failed to import Flickr Keys')
else:
    print('One or more Flickr Key values have not been entered in secret.py')

