import snscrape.modules.twitter as sntwitter
import pandas as pd 
from time import sleep 
import tweepy

tweets_data = []

username = input("Enter your keyword :")
number = int(input("How many tweets do you want to scrape :"))

for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
	if i > number:
		break
	tweets_data.append([tweets.date, tweets.content, tweets.user.username, tweets.url])



df = pd.DataFrame(tweets_data,columns=['Date','Tweets','Username','Url'])
df.to_csv(f'{username}.csv', index=False, encoding='utf-8')
