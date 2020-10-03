from tkinter import *
from functions import *
from tweetdb import *
from client import client

root = Tk()

def execute():
    #Checks if database is created
    createDb()
    # Check if integer was entered
    try:
        int(num.get())
        numCheck.config(text = "Tweet data recorded")
        # Parse num of tweets based on query into class
        foo = client(query.get(), num.get())
        foo.searchTweets()
        createTweetsArray(foo.tweets)
        # Insert data into Sqlite
        insertDb(foo.tweets)
        foo.tweets.clear()
        # Delete entry data
        num.delete(0,END)
        query.delete(0,END)
        # Commit changes to database
        conn.commit()
    except ValueError:
        numCheck.config(text = "Enter a valid integer")
        num.delete(0,END)

# Create text boxes
num = Entry(root, width=30)
num.grid(row=0, column=1, padx=20)

numCheck = Label(root, text='')
numCheck.grid(row=1, column=1, padx=20)

query = Entry(root, width=30)
query.grid(row=2, column=1, padx=20)

# Create text box labels
num_label = Label(root, text="Number")
num_label.grid(row=0, column=0, padx=20)
query_label = Label(root, text="Query")
query_label.grid(row=2, column=0, padx=20)

# Create submit button
search_btn = Button(root, text="Search for tweets", command=execute)
search_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

root.mainloop()

# Close database connection
conn.close()
