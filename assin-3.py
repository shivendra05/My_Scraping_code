import tweepy
import csv

ckey = 'key'
csecret = 'key'
atoken = 'key'
asecret = 'key'


auth = tweepy.auth.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

csvFile = open('a.csv', 'ab')
csvWriter = csv.writer(csvFile)


stuff = api.user_timeline(screen_name = 'Tata Communications AT&T\
Level 3\
BT Global Services\
Telstra', count = 1)



for status in stuff:
    print status.author, status.user
