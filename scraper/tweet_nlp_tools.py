"""A tool for cleaning and applying NLP tools to gathered tweets."""

import pandas as pd


def convert_to_dataframe(tweets):
    """Converts a tweepy.resultSet object into a pandas.DataFrame"""
    data_dicts = [
        {
            "tweet_id": tweet.id,
            "username": tweet.author.screen_name,
            "created_at": tweet.created_at,
            "hashtags": tweet.entities.get("hashtags"),
            "user_mentions": tweet.entities.get("user_mentions"),
            "symbols": tweet.entities.get("symbols"),
            "favorite_count": tweet.favorite_count,
            "language": tweet.lang,
            "retweet_count": tweet.retweet_count,
            "screen_name": tweet.source,
            "text": tweet.text,
            "location": tweet.user.location,
        }
        for tweet in tweets
    ]

    return pd.DataFrame(data_dicts)
