import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':
  
  keyword1 = "Bitcoin"
  
  try:
     
     #keyword-1 Grabber
     keyword1Grabber = TwitterGrabber(keyword1)  
     keyword1Grabber.streamTweets()
     print(Fore.GREEN + "\nStreaming started on ",  keyword1)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
