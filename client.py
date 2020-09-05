import tweepy

consumer_key = 'eBKSNsuffFGsACqyysXPWKxRW'
consumer_key_secret = 'cA1XKwamNZffGH3kwnPOUqzGxvmHNBv2FnGQuheuOfyWK2t83r'

access_key = '1244001951437783042-aGFfqnQ2DyJ1Fvb8mg10TZHV3lz1gZ'
access_key_secret = 'mKiveaLNNn4ouf9h2eiDLyZ9izc0yvZ9h67F2TjabCWkP'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_key, access_key_secret)

api = tweepy.API(auth)

class client:

    def __init__(self, query='', count=10, tweets=[]):
        self.query = query
        self.count = count
        self.tweets = tweets

    def searchTweets(self):
        parsedTweets = api.search(q=self.query, count=self.count)
        for tweet in parsedTweets:
            if tweet not in self.tweets:
                self.tweets.append(tweet.text)


