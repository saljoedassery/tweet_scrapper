# -*- coding: utf-8 -*-
import scrapy
import re

class TweetScrapperSpider(scrapy.Spider):
    name = 'tweet_scrapper'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/FIFAWorldCup/']

    def parse(self, response):
        tweets = response.css('p.TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text').extract()
        f = open('tweets.txt','a')
        for tweet in tweets:
            text = tweet.encode("ascii","ignore")
            text = re.sub('^<.*?>', '',text)
            text = re.sub('<a href=.*?>', '',text)
            text = re.sub('<span.*?>', '',text)
            text = re.sub('<b>|<s>|<a>|</b>|</s>|</a>', '',text)
            text = re.sub('<.*?>', '',text)
            text = re.sub('\n', ' ',text)
            text = text+"\n"
            f.write(text)
        f.close()