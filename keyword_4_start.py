import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':

  keyword4 = "Cryptocurrency"  


  try:

      #keyword-4 Grabber
     keyword4Grabber = TwitterGrabber(keyword4)  
     keyword4Grabber.streamTweets()
     print(Fore.MAGENTA + "\nStreaming started on ",  keyword4)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
