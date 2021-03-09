import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':

  keyword7 = "GOOG"


  try:
     
      #keyword-7 Grabber
     keyword7Grabber = TwitterGrabber(keyword7)  
     keyword7Grabber.streamTweets()
     print(Fore.BLUE + "\nStreaming started on ",  keyword7)



  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
