import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'economist'
	allowed_domains = ["economist.com"]
	start_urls = ['https://www.economist.com/the-world-this-week/rss.xml',
	'https://www.economist.com/letters/rss.xml',
	'https://www.economist.com/leaders/rss.xml',
	'https://www.economist.com/briefing/rss.xml',
	'https://www.economist.com/special-report/rss.xml',
	'https://www.economist.com/britain/rss.xml',
	'https://www.economist.com/europe/rss.xml',
	'https://www.economist.com/united-states/rss.xml',
	'https://www.economist.com/the-americas/rss.xml',
	'https://www.economist.com/middle-east-and-africa/rss.xml',
	'https://www.economist.com/asia/rss.xml',
	'https://www.economist.com/china/rss.xml',
	'https://www.economist.com/international/rss.xml',
	'https://www.economist.com/business/rss.xml',
	'https://www.economist.com/finance-and-economics/rss.xml',
	'https://www.economist.com/science-and-technology/rss.xml',
	'https://www.economist.com/books-and-arts/rss.xml',
	'https://www.economist.com/obituary/rss.xml',
	'https://www.economist.com/graphic-detail/rss.xml',
	'https://www.economist.com/economic-and-financial-indicators/rss.xml']
	# iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
	itertag = 'item'

	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

		item = {}
		item['title'] = node.xpath('title/text()',).extract()
		item['link'] = node .xpath('link/text()',).extract()
		item['description'] = node.xpath('description/text()',).extract()
		# item['title'][0] = item['title'][0].replace("\"","")
		item['source'] = "The Economist"
		tab = response.url
		# # tab = tab.replace(".rss", "")
		tab = tab.replace("https://www.economist.com/", "")
		tab = tab.replace("/rss.xml", "")

		item['tab'] = tab
		item['date'] = node.xpath('pubDate/text()',).extract()
		# print(item["title"])
		return item
