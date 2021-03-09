import tweepy

##Declaring the Auth Credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

class TAuth:
    ##As clear from name for Authentication
    def authenticate(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth;
  
   