# Reddit_comments_on_nus_hostels
A very basic sentiment analysis on reddit comments about nus hostels


In this project I applied basic sentiment analysis on reddits comemnts on posts related to hostels on the National University of Singapore's campus to count the number of positive and negative comments on each type of hostels. I used the Reddit API praw to retrive the comments and TextBlob to perform sentiment analysis, which gives a score that is either a positive or negative to measure how positive is the comment.


Since the programme's way of handling sentiment analysis is still very crude, it does mistake comments that are polite responses such as "Thank you very much!" as overly positive and comments that are rejection such as "Nah I don't think so" as overly negative despites them not contrinuting to the assessment of the hostels. In addition, sich the programme only categorised each comment on each post, it couldn't tell in comments that compare two or more hostels which hostel was mentioned more favorably. Thus, the accucracy of the result shoudln't be taken too seriously as the project is only done out of curiosity with little scientific rigour. 


Still, it was quite fun to do and I hope the outcome is interesting. :)
