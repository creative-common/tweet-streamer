import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':

  keyword3 = "Coindesk"
 

  try:
     
      #keyword-3 Grabber
     keyword3Grabber = TwitterGrabber(keyword3)  
     keyword3Grabber.streamTweets()
     print(Fore.YELLOW + "\nStreaming started on ",  keyword3)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
