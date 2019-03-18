# Infinity-Snap


Perfect Balance on twitter


```
python3 main.py

```


![](https://cdn-images-1.medium.com/max/1600/1*lZT_ycFG-r9-j0TYS7SUaQ.png)

In real World we dont have infinity stones. There is no snap to remove half of the living, but We have something better: Virtual World! We can create what ever we want, and we can destroy what ever we want. This situation makes us a Thanos like titans who holds the infinity gauntlet.

This being said, I though it would be fun to delete randomly fifty percent of my posts in social media. It was one of my stupidest idea but who cares and I thought it would be even more idiotic to actually share the code I used. So let me walk you through.

First we need to get Twitter API access. Get an account to from [https://developer.twitter.com/](https://developer.twitter.com/en/apps) and create a new app. After that point you should have 4 code. API key, API secret key, Access token and Access token secret. If you have them rest is easy!

```python
# Get the environment ready
import tweepy
auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)
```

Now, just get the tweets and tweet ids.

```python
tweet_ids = []
tweets = {}
for status in tweepy.Cursor(api.user_timeline).items():
    tweet_ids.append(status.id)
    tweets[status.id] = [status.text, status.favorite_count]
```

Now we need a balance :Smile:

![](https://cdn-images-1.medium.com/max/1600/1*VUx-0Ou4ZRr7x_8hrIoxPw.gif)

```python
# Randomly change the places
random.shuffle(tweet_ids)
removed_tweets = []
# Get and delete first half :D 
for i in range(len(tweet_ids)//2):
    removed_tweets.append(tweets[tweet_ids[i]])
    api.destroy_status(tweet_ids[i])
```



Or if you don't wanna do all that I have a repository that you can use:

[Repository Link](https://github.com/AhmetHamzaEmra/Infinity-Snap)

It runs with flask and displays deleted tweets.

![](https://cdn-images-1.medium.com/max/1600/1*p_vgdl_Fh-fl6KEJKMFkGQ.png)

This is all I wanna share for now. See you until I have another “good” idea 😂
