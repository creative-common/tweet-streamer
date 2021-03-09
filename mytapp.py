import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth


class TwitterGrabber:
    def __init__(self, keyword):
        print("keyword received is " + keyword)
        self.keyword = keyword

    def streamTweets(self):
        tweetListener = TweetListener(self.keyword)
        #call TAuth Constructor
        tauth = TAuth()
        #do auth
        auth = tauth.authenticate()
        tStream = tweepy.Stream(auth = auth, listener=tweetListener, tweet_mode='extended')
        tStream.filter(track=[self.keyword])
       