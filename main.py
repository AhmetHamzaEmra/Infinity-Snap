from __future__ import absolute_import, division, print_function
import tweepy
import random
from flask import render_template, Flask, request
import flask
import os


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath("app.py"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    
	API_key = request.form['API_key']
	API_secret_key = request.form['API_secret_key']

	Access_token = request.form['Access_token']
	Access_token_secret = request.form['Access_token_secret']

	auth = tweepy.OAuthHandler(API_key, API_secret_key)
	auth.set_access_token(Access_token, Access_token_secret)
	api = tweepy.API(auth)

	tweet_ids = []
	tweets = {}
	for status in tweepy.Cursor(api.user_timeline).items():
		tweet_ids.append(status.id)
		tweets[status.id] = [status.text, status.favorite_count]

	random.shuffle(tweet_ids)
	removed_tweets = []
	for i in range(len(tweet_ids)//2):
		removed_tweets.append(tweets[tweet_ids[i]])
		# api.destroy_status(tweet_ids[i]) # uncommend this part if you realy wanna delete :D 
		
	return render_template("result.html" ,tweets=removed_tweets)

if __name__ == "__main__":
    app.run(debug=True)