from client import client

def main():
    num = int(input('Enter a number: '))
    search = input('Enter a query:')

    foo = client(search, num)
    foo.getTweets()
    foo.checkPolarity()

if __name__ == '__main__':
    main()

