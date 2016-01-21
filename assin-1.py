import tweepy
import csv
import re
import json

ckey = 'key'
csecret = 'key'
atoken = 'key'
asecret = 'key'


auth = tweepy.auth.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)



print '-------@@@@@@@@@@@@---------------DeutscheBank-------@@@@@@@@@@@-----------------'

for tweet in tweepy.Cursor(api.search,
                           q = "Deutche Bank ",
                           since = "2015-12-14",
                           screen_name = "Deutche Bank Kim Hammonds Henry Ritchotte",
                           until = "2015-12-15",
                           lang = "en").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text



print '-------@@@@@@@@@@@@---------------UNILEVER-------@@@@@@@@@@@-----------------'

for tweet in tweepy.Cursor(api.search,
                           q = "UNILEVER",
                           since = "2015-12-14",
                           screen_name = "Paul Polman Pier Luigi Jane Moran",
                           until = "2015-12-15",
                           lang = "en", count=1).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
    


print '-------@@@@@@@@@@@@---------------DHL Group-------@@@@@@@@@@@-----------------'

for tweet in tweepy.Cursor(api.search,
                           q = "DHL Group",
                           since = "2015-12-14",
                           screen_name = "Frank Appel",
                           until = "2015-12-15",
                           lang = "en").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text

csvFile.close()
