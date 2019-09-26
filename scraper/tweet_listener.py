"""A class that will handle ingestion of tweets"""
import csv
import sys

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

    def write_to_csv(self, status):
        f = open(self.output_file, "a")
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(status)
        f.close()
