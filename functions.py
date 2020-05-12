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

def getTweets(query, count=10):
    fetchedTweets = api.search(q = query, count = count)
    parsedTweets = []
    for tweet in fetchedTweets:
        parsedTweets.append(tweet.text)
    return parsedTweets

def polarityCheck(a):
    sentimentN = []
    sentimentP = []
    sentimentNe = []
    for tweet in a:
        testimonial = TextBlob(tweet)
        if testimonial.sentiment.polarity > 0:
            sentimentP.append(tweet)
        if testimonial.sentiment.polarity < 0:
            sentimentN.append(tweet)
        if testimonial.sentiment.polarity == 0:
            sentimentNe.append(tweet)
    print('Percentage of positive tweets:' + str(float(len(sentimentP) / (len(sentimentN) + len(sentimentP) + len(sentimentNe)))*100))
    print('Percentage of negative tweets:' + str(float(len(sentimentN) / (len(sentimentN) + len(sentimentP) + len(sentimentNe)))*100))
    print('Percentage of neutral tweets:' + str(float(len(sentimentNe) / (len(sentimentN) + len(sentimentP) + len(sentimentNe)))*100))