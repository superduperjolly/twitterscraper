"""The old module for downloading tweets. I have no idea if this still works."""
import tweepy
import json
import csv


CONSUMER_KEY = "XBxOau9zslm4SPufu2k1fBIhc"
CONSUMER_SECRET = "uCpf8Hw25QWuCnXgy46pGwaKFxmacuW2kPuftqUXM4hPVy3p3K"
ACCESS_TOKEN = "598146812-xKl8cwyH6QivL6UnRiPWbhb0gWNr3gWHM8iLlNF3"
ACCESS_TOKEN_SECRET = "0jrSuHO5PV9CNjrdw9q3QE7IVCsogofBKWOCGuQEkn2Vm"


class StreamListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        # print('@%s: %s in: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore'), tweet['place']))

        print(
            "Tweeted on %s in %s: @%s: %s"
            % (
                tweet["created_at"],
                tweet["place"]["full_name"],
                tweet["user"]["screen_name"],
                tweet["text"].encode("ascii", "ignore"),
            )
        )
        print(
            "Stats: REP_COUNT=%s, RET_COUNT=%s, FAV_COUNT=%s"
            % (tweet["reply_count"], tweet["retweet_count"], tweet["favorite_count"])
        )

        write_row(
            (
                tweet["created_at"],
                tweet["place"]["full_name"],
                tweet["user"]["screen_name"],
                tweet["text"],
                tweet["reply_count"],
                tweet["retweet_count"],
                tweet["favorite_count"],
            )
        )

        # created_at
        # id
        # text
        # source
        # user
        # geo
        # place
        # reply_count
        # retweet_count
        # favorite_count
        # lang

    def on_error(self, status):
        print(status)

    def on_limit(self, track):
        print("Limit hit! Track = %s" % track)


def write_row(values):
    print(values)
    f = open("tweets.csv", "a")
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(values)
    f.close()


if __name__ == "__main__":
    listener = StreamListener()
    # manila = [120.906211, 14.348096, 121.135076, 14.787496]
    # manila = [120.957243821,14.4914889863,121.1028126687,14.6729047449]
    manila = [120.936813, 14.488869, 121.100578, 14.665969]

    print("Printing tweets in Manila...")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, listener)
    stream.filter(locations=manila)
