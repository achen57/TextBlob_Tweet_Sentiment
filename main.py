from client import client
from functions import *
from tweetdb import *

def main():
    num = int(input('Enter a number: '))
    search = input('Enter a query: ')

    foo = client(search, num)
    foo.searchTweets()

    createTweetsArray(foo.tweets)

    insertDb(foo.tweets)
    displayDb()

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

