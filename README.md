# TodayWasAGoodDay
A simple twitter bot that tweets today was a good day if the White Sox win and the Cubs lose

## Implementation
This bot was made using a python script that tweets to this account https://twitter.com/bot_sox.

## Creating your own bot
Feel free to use this as a template for you own twitter bot. I used mlbgame which is an mlb api to see the results of the games. Its documentation can be found at http://panz.io/mlbgame/. I also used tweepy as a twitter api http://docs.tweepy.org/en/latest/. To get the access keys and tokens for twitter you must apply for a twitter developer account.

## Deployment
This bot is currently deployed as an AWS Lambda function. The code is slightly modified from the code in this repo in order to run properly with lambda.
