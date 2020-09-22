#import tweepy
import datetime
import mlbgame

#consumer_key = 
#consumer_secret = 
#access_token = 
#access_token_secret =

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#twApi = tweepy.API(auth)

def main:
    today = datetime.date.today()
    daySox = mlbgame.day(today.year, today.month, today.day, home='White Sox', away='White Sox')
    dayCubs = mlbgame.day(today.year, today.month, today.day, home='Cubs', away='Cubs')
    soxWin = true
    cubsLose = true
    if daySox && dayCubs:
        for game in daySox:
            
