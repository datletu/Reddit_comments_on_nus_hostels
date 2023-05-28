import praw
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt


# Subreddit and search keyword

subreddit_name = "nus"
search_keywords = ['raffles hall', 'ke7', 'rc4', 'utown residence','pgpr']
positive = []
negative = []

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="YOUR ID",
    client_secret="YOUR SECRET",
    user_agent="t",
    read_only = True
)

# Get subreddit
subreddit = reddit.subreddit(subreddit_name)
for search_keyword in search_keywords:
    positive_count = 0
    negative_count = 0
    # Search posts mentioning 'raffles hall'
    posts = subreddit.search(search_keyword, time_filter="year", limit = 20)


    for post in posts:
        post.comments.replace_more(limit=None)  # Retrieve all comments
        comments = post.comments.list()
        print(post.title)

        # Check sentiment of comments
        for comment in comments:
            comment_text = comment.body

            blob = TextBlob(comment_text)
            sentiment = blob.sentiment.polarity
            with open('record2.txt', 'a', encoding='utf-8') as f:
                f.write(comment_text)
                f.write('\n')
                f.write(str(sentiment))
                f.write('\n')
                f.write('\n')
            if sentiment > 0.22:
                positive_count += 1
                
                
            elif sentiment < -0.2:
                negative_count += 1
    positive.append(positive_count)
    negative.append(negative_count)


    print(search_keyword)
    print("Positive comments count:", positive_count)
    print("Negative comments count:", negative_count)

plt.bar(search_keywords, negative, color='r')
plt.bar(search_keywords, positive, bottom=negative, color='b')
plt.xlabel("Hostels")
plt.ylabel("Number of comments")
plt.legend(['negative','positive'])
plt.show()