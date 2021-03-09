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
    
    #   #keyword-2 Grabber
     keyword2Grabber = TwitterGrabber(keyword2)  
     keyword2Grabber.streamTweets()
     print(Fore.GREEN + "\nStreaming started on ",  keyword2)

  except KeyboardInterrupt:
     print('\n\n  ' + Fore.RED + 'Streaming Stopped')
 
