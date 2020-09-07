import sqlite3

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

#c.execute("""CREATE TABLE tweets (
#           Username text,
#           Tweet text,
#           Polarity float,
#           Sentiment text)""")

def insertDb(arr):
    for i in range(len(arr)):
        c.execute("INSERT INTO tweets VALUES (?, ?, ?, ?)", (arr[i][0], arr[i][1], arr[i][2], arr[i][3]))

def displayDb():
    c.execute("SELECT * FROM tweets")
    print(c.fetchall())



