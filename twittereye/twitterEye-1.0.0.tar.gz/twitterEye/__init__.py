import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt


def _authenticate_twitter(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
    api = None

    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except:
        print("Twitter Authentication Failed, please verify your secret keys")
        return False


def _get_tweets(api, query: str, count: int) -> list:
		tweets = []

		try:
			fetched_tweets = api.search_tweets(q = query, count = count)

			for tweet in fetched_tweets:
				parsed_tweet = {}

				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = _get_tweet_sentiment(tweet.text)

				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets
		except:
			print("Error while fetching tweets from twitter")


def _clean_tweet(tweet: str) -> str:
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def _get_tweet_sentiment(tweet: str) -> str:
	try:
		cleaned_tweet = _clean_tweet(tweet)
		analysis = TextBlob(cleaned_tweet)
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'
	except:
		pass


def _classify_emotions_in_percentage(tweets: list) -> dict:
	try:
		positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
		positive_sentiments_percentage = (100*len(positive_tweets)/len(tweets))
		
		negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
		negative_sentiments_percentage = (100*len(negative_tweets)/len(tweets))
		
		neutral_sentiments_percentage = (100*(len(tweets) -(len( negative_tweets )+len( positive_tweets)))/len(tweets))
		
		return {'Positive':positive_sentiments_percentage,
		'Negative':negative_sentiments_percentage, 'Neutral':neutral_sentiments_percentage} 
	except:
		print("Error while generating emotions percentage based report")


def _visualize_data(data: dict, keyword: str) -> None:
	try:
		emotions = list(data.keys())
		percentage = list(data.values())
		
		fig = plt.figure(figsize = (10, 5))
		plt.bar(emotions, percentage, color ='maroon',
				width = 0.4)
		plt.xlabel("Emotions Analyzed")
		plt.ylabel("Emotions Frequency Percentage")
		plt.title(f"Sentimental Analysis of keyword: {keyword}")
		plt.show()
	except:
		print("Error while visualizing results")


def analyze_keyword(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str, keyword: str, tweets_limit: int = 1000, visualize: bool = True):
	try:
		api = _authenticate_twitter(consumer_key, consumer_secret, access_token, access_token_secret)
		tweets = _get_tweets(api, keyword, tweets_limit)
		plot_data = _classify_emotions_in_percentage(tweets)
		if visualize:
			_visualize_data(plot_data, keyword)
		return plot_data	
	except:
		print("Error while analyzing keyword")
