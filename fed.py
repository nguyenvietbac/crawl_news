import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'fed'
	allowed_domains = ["federalreserve.gov"]
	start_urls = ['https://www.federalreserve.gov/feeds/press_all.xml']
	# iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
	itertag = 'item'

	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

		item = {}
		item['title'] = node.xpath('title/text()',).extract()
		item['link'] = node .xpath('link/text()',).extract()
		item['description'] = node.xpath('description/text()',).extract()
		# item['title'][0] = item['title'][0].replace("\"","")
		item['source'] = "Federal Reserve(FED)"
		tab = ""
		# # tab = tab.replace(".rss", "")
		# tab = tab.replace("https://www.economist.com/", "")
		# tab = tab.replace("/rss.xml", "")

		item['tab'] = tab
		item['date'] = node.xpath('pubDate/text()',).extract()
		# print(item["title"])
		return item
