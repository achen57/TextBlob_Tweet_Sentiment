from textblob import TextBlob


def createTweetsArray(arr):
    tempList = []
    for i in range(len(arr)):
        testimonial = TextBlob(arr[i])
        tempList.append(arr[i][3:arr[i].find(":")])
        tempList.append(arr[i][arr[i].find(":") + 2:])
        tempList.append(testimonial.sentiment.polarity)
        if testimonial.sentiment.polarity > 0:
            tempList.append('Positive')
        elif testimonial.sentiment.polarity == 0:
            tempList.append('Neutral')
        else:
            tempList.append('Negative')
        arr[i] = tempList
        tempList = []



