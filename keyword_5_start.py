import tweepy
from colorama import init, Fore, Back, Style

from tlistener import TweetListener
from auth import TAuth
from mytapp import TwitterGrabber

       

if __name__ == '__main__':
  keyword1 = "Bitcoin"
  keyword2 = "Altcoin"  
  keyword3 = "Coindesk"
  keyword4 = "Cryptocurrency"  
  keyword5 = "Gold"
  keyword6 = "APPL"  
  keyword7 = "GOOG"
  keyword8 = "YHOO"  

  try:
      #keyword-5 Grabber
     keyword5Grabber = TwitterGrabber(keyword5)  
     keyword5Grabber.streamTweets()
     print(Fore.CYAN + "\nStreaming started on ",  keyword5)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
