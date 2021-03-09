import tweepy
import os
import sys
from datetime import datetime
import csv
from colorama import init, Fore, Back, Style
from tweepy.streaming import StreamListener
import json
import re #for regex
import string

class TweetListener(StreamListener):
 
    def __init__(self, keyword):
        super(TweetListener, self).__init__()
        print("Tweetlistener keyword is " + keyword)
        self.keyword = keyword

    def cleanData(self, text):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        
        text = regrex_pattern.sub(r'',text)

        # remove numbers
        text_nonum = re.sub(r'\d+', '', text)
        # remove punctuations and convert characters to lower case
        text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
        # substitute multiple whitespace with single whitespace
        # Also, removes leading and trailing whitespaces
        text_no_doublespace = re.sub('\s+', ' ', text_nopunct).strip()
        # remove non english letters from string
        clean_text =  re.sub("[^a-zA-Z0-9]+", "",text_no_doublespace)

        return text_no_doublespace

    def on_status(self, status):

        if hasattr(status, 'retweeted_status'): # ignore retweets
            #sys.stdout.write("Retweet, Ignore \n")
            return
        if not status.lang == "en": # You can ignore language here, or you can do it before calling the streamer
            sys.stdout.write('\n ' + Fore.RED + "Not English, Ignore \n")
            return

        tweet_object = status

        # Checks if its a extended tweet (>140 characters)
        if 'extended_tweet' in tweet_object._json:
            tweet_text = tweet_object.extended_tweet['full_text']
        else:
            tweet_text = tweet_object.text

        '''Convert all named and numeric character references
        (e.g. &gt;, &#62;, &#x3e;) in the string s to the
        corresponding Unicode characters'''
        tweet_text = (tweet_text.replace('&amp;', '&').replace('&lt;', '<')
                  .replace('&gt;', '>').replace('&quot;', '"')
                  .replace('&#39;', "'").replace(';', " ")
                  .replace(r'\u', " "))

        '''Remove all the emojis'''
        tweet_text = self.cleanData(tweet_text)

        tweetlist = []
        tweetdict = {
            "Tweet_ID": str(status.id),
            "Text": str(tweet_text),
            "Created_At": str(status.created_at),
            "User_ID": status.user.id_str,
            } 
        tweetlist.append(tweetdict)
        print('\n\n  ' + Fore.WHITE + str(tweetlist))
        with open(self.keyword+'.csv', 'a', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([str(status.id), str(tweet_text), status.user.id_str, str(status.created_at)])
        tweetlist = []

    def on_error(self, status):
       print(status)