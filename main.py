from functions import getTweets, polarityCheck

def main():
    num = int(input('Enter a number: '))
    search = input('Enter a query: ')

    polarityCheck(getTweets(search, num))

if __name__ == '__main__':
    main()
