from textblob import TextBlob


def trimTweets(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][arr[i].find(":") + 1:]

def assignPolarity(arr):
    tempList = []
    for i in range(len(arr)):
        testimonial = TextBlob(arr[i])
        tempList.append(testimonial.sentiment.polarity)
        tempList.append(arr[i])
        arr[i] = tempList
        tempList = []


