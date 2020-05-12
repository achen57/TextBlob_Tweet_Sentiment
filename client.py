import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

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

    def getTweets(self):
        parsedTweets = api.search(q=self.query, count=self.count)
        for tweet in parsedTweets:
            if tweet not in self.tweets:
                self.tweets.append(tweet.text)

    def checkPolarity(self):
        sentimentP = []
        sentimentN = []
        sentimentNe = []
        for tweet in self.tweets:
            testimonial = TextBlob(tweet)
            if testimonial.sentiment.polarity > 0:
                sentimentP.append(tweet)
            if testimonial.sentiment.polarity < 0:
                sentimentN.append(tweet)
            if testimonial.sentiment.polarity == 0:
                sentimentNe.append(tweet)
        print('Percentage of positive tweets:' + str(
            float(len(sentimentP) / (len(sentimentN) + len(sentimentP) + len(sentimentNe))) * 100))
        print('Percentage of negative tweets:' + str(
            float(len(sentimentN) / (len(sentimentN) + len(sentimentP) + len(sentimentNe))) * 100))
        print('Percentage of neutral tweets:' + str(
            float(len(sentimentNe) / (len(sentimentN) + len(sentimentP) + len(sentimentNe))) * 100))

