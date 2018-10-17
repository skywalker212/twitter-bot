import requests
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ['API_KEY']
api_url = os.environ['API_URL']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

def get_quote():
    headers = {'X-Mashape-Key': api_key, 'X-Mashape-Host': api_url}
    response = requests.get(api_url, headers=headers)
    json = response.json()[0]
    tweet = json['quote']+ '\n- ' + json['author'] +' #dailyQuote'
    return tweet

def tweet_quote():
    tweet = get_quote()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.update_status(tweet)
    print(status.id) 

tweet_quote()