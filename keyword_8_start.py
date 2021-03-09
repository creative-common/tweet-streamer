import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':
 
  keyword8 = "COVID19"  

  try:
     
      #keyword-8 Grabber
     keyword8Grabber = TwitterGrabber(keyword8)  
     keyword8Grabber.streamTweets()
     print(Fore.MAGENTA + "\nStreaming started on ",  keyword8)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
