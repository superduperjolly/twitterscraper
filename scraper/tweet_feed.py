"""A set of functions to gather and clean twitter data."""
import tweepy

from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)


# Authenticate the package
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# initialize API
api = tweepy.API(auth)


def get_tweets_by_user(username):
    """Gets a set of tweets by a specific user within a timeframe"""
    pass


def get_tweets_on_timeline():
    """Gets tweets in my timeline"""
    public_tweets = api.home_timeline()



def get_tweets_in_area(coordinates):
    """Gets tweets in an area. Take note that twitter allows
    'boxing' an area for retrieving tweets. Meaning it's expecting
    a list of 4 coordinates to indicate the supported area.
    
    :param: coordinates
    :dtype: list
    :return:"""
    pass


def steam_tweets_now(coordinates):
    """Gets tweets being published at the moment."""
    pass
