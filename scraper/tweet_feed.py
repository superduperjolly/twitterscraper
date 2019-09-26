"""A set of functions to gather and clean twitter data."""
import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

from scraper.tweet_listener import Listener


# Authenticate the package
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# initialize API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_tweets_by_user(username):
    """Gets a set of tweets by a specific user within a timeframe"""
    pass


def get_tweets_on_timeline(since_id, count):
    """Gets tweets in my timeline"""
    public_tweets = api.home_timeline(since_id=since_id, count=count)
    return public_tweets


def get_tweets_in_area_now(
    coordinates=[120.936813, 14.488869, 121.100578, 14.665969],
    filepath="data/tweets.csv",
):
    """Gets tweets in an area. Take note that twitter allows
    'boxing' an area for retrieving tweets. Meaning it's expecting
    a list of 4 coordinates to indicate the supported area.
    
    :param: coordinates
    :dtype: list
    :return:"""
    listener = Listener(output_file=filepath)
    stream = tweepy.Stream(auth=api.auth, listener=listener)

    try:
        print("Streaming tweets in location %s and saving to %s" % (coordinates, filepath))
        stream.sample(locations=coordinates)
    except KeyboardInterrupt:
        print("Streaming stopped.")
    finally:
        print("Done. See '%s' for collected tweets" % filepath)
        stream.disconnect()
