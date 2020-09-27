import tweepy
import datetime
import mlbgame
from dateutil import tz

consumer_key = NOTCONSUMERKEY
consumer_secret = NOTCONSUMERSECRET
access_token = NOTACCESSTOKEN
access_token_secret = NOTACCESSTOKENSECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twApi = tweepy.API(auth)

def main():
    cst = tz.gettz('America/Chicago')
    today = datetime.datetime.now(cst)
    daySox = mlbgame.day(today.year, today.month, today.day, home='White Sox', away='White Sox')
    dayCubs = mlbgame.day(today.year, today.month, today.day, home='Cubs', away='Cubs')
    soxWin = 0
    cubsLose = 0
    if daySox and dayCubs:
        soxWin = 1
        cubsLose = 1
        for game in daySox:
            if game.game_status != 'FINAL' or game.w_team != 'White Sox':
                soxWin = 0
        
        for game in dayCubs:
            if game.game_status != 'FINAL' or game.w_team == 'Cubs':
                cubsLose = 0

    if soxWin == 1 and cubsLose == 1:
        tweet = "Today was a good day, the Sox won and the Cubs lost"
        twApi.update_status(tweet)



if __name__ == "__main__":
    main()
