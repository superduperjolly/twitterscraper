"""A class that will handle ingestion of tweets"""
import csv
import sys

import pandas as pd
from tweepy.streaming import StreamListener


class Listener(StreamListener):
    """Custom listener class."""

    def __init__(self, output_file=sys.stdout):
        super(Listener, self).__init__()
        self.output_file = output_file

    def on_status(self, status):
        print(status.text)
        self.write_to_csv(status)

    def on_error(self, status_code):
        print(status_code)
        return False

    def write_to_csv(self, tweet):
        df = pd.DataFrame(
            [
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
                    "user_location": tweet.user.location,
                    "tweet_location": tweet.place.full_name,
                }
            ]
        )

        with open(self.output_file, "a") as f:
            df.to_csv(
                f, header=(f.tell() == 0), quoting=csv.QUOTE_NONNUMERIC, index=False
            )
