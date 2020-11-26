# RaspberryPi-Twitterbot
Simple Twitter bot for Raspberry Pi to get you started. Written with Python.
## Twitter developer account

First thing you need to do is to create a twitter developer account. You can do that here, https://developer.twitter.com/en . Make sure to fill in the right information. Also make sure to test api endpoints, when prompted. And take a copy of those.

## App permissions

Make sure to give your app the right permissions. I think they should be read, write and direct messages.

## Authentication settings

Enable the 3-legged OAuth, with example callback and website urls. They can be for example https://google.com.

## Authentication Tokens

For the app to work, we need access tokens and secrets, you can generate those on the developer portal at, projects & apps -> your project name -> keys and tokens. Make sure to copy these also, because we need them later on.

Now that we have everything good to go, it's time to set up the Raspberry Pi.

## Raspberry Pi

Make sure your Raspberry Pi is up to date, with the following commands.

sudo apt update
sudo apt upgrade

Then install tweepy, it's a python library for twitter api.

pip install Tweepy

## Create the python file to test and execute

You can do this basically with a text editor you want. I used gedit. Then save it for example like tweetbot.py

You can run this with the following command,

python tweetbot.py

## Questions or feedback

for any questions or feedback, you can contact me at jussi.k.jokinen [ at ] gmail.com.