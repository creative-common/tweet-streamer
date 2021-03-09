import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':

  keyword6 = "APPL"  
 
  try:
    
      #keyword-6 Grabber
     keyword6Grabber = TwitterGrabber(keyword6)  
     keyword6Grabber.streamTweets()
     print(Fore.GREEN + "\nStreaming started on ",  keyword6)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
