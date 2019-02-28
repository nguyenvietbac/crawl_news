import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'reuters'
	allowed_domains = ["reuters.com"]
	start_urls = ['http://feeds.reuters.com/news/artsculture',
	'http://feeds.reuters.com/reuters/businessNews',
	'http://feeds.reuters.com/reuters/companyNews',
	'http://feeds.reuters.com/reuters/entertainment',
	'http://feeds.reuters.com/reuters/environment',
	'http://feeds.reuters.com/reuters/healthNews',
	'http://feeds.reuters.com/reuters/lifestyle',
	'http://feeds.reuters.com/news/wealth',
	'http://feeds.reuters.com/reuters/oddlyEnoughNews',
	'http://feeds.reuters.com/ReutersPictures',
	'http://feeds.reuters.com/reuters/peopleNews',
	'http://feeds.reuters.com/Reuters/PoliticsNews',
	'http://feeds.reuters.com/reuters/scienceNews',
	'http://feeds.reuters.com/reuters/sportsNews',
	'http://feeds.reuters.com/reuters/technologyNews',
	'http://feeds.reuters.com/reuters/topNews',
	'http://feeds.reuters.com/Reuters/domesticNews',
	'http://feeds.reuters.com/Reuters/worldNews',
	'http://feeds.reuters.com/reuters/USVideoBreakingviews',
	'http://feeds.reuters.com/reuters/USVideoBusiness',
	'http://feeds.reuters.com/reuters/USVideoEntertainment',
	'http://feeds.reuters.com/reuters/USVideoEnvironment',
	'http://feeds.reuters.com/reuters/USVideoLifestyle',
	'http://feeds.reuters.com/reuters/USVideoLatest',
	'http://feeds.reuters.com/reuters/USVideoNewsmakers',
	'http://feeds.reuters.com/reuters/USVideoOddlyEnough',
	'http://feeds.reuters.com/reuters/USVideoPersonalFinance',
	'http://feeds.reuters.com/reuters/USVideoPolitics',
	'http://feeds.reuters.com/reuters/USVideoRoughCuts',
	'http://feeds.reuters.com/reuters/USVideoTechnology',
	'http://feeds.reuters.com/reuters/USVideoTopNews',
	'http://feeds.reuters.com/reuters/USVideoWorldNews']
	# iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
	itertag = 'item'

	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

		item = {}
		item['title'] = node.xpath('title/text()',).extract()
		item['link'] = node .xpath('link/text()',).extract()
		item['description'] = node.xpath('description/text()',).extract()
		# item['title'][0] = item['title'][0].replace("\"","")
		item['source'] = "Reuters"
		tab = response.url
		# # tab = tab.replace(".rss", "")
		tab = tab.replace("http://feeds.reuters.com/", "")
		# tab = tab.replace("/", ",")

		item['tab'] = tab
		item['date'] = node.xpath('pubDate/text()',).extract()
		# print(item["title"])
		return item
