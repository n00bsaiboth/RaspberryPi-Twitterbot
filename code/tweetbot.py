import os
import tweepy as tp
from time import sleep

# this is just a simple test script, nothing more, nothing less.

# fill your api keys and access tokens

consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_secret = 'your-access-secret'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tp.API(auth)

user = api.me()

print(user.name)
print(user.location)