from client import client
from functions import *

def main():
    num = int(input('Enter a number: '))
    search = input('Enter a query: ')

    foo = client(search, num)
    foo.getTweets()
    trimTweets(foo.tweets)
    assignPolarity(foo.tweets)

    print(foo.tweets)

if __name__ == '__main__':
    main()

