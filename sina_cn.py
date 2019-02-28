import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'sina'
	allowed_domains = ["rss.sina.com.cn"]
	start_urls = ['http://rss.sina.com.cn/roll/finance/hot_roll.xml',
	]
	# iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
	itertag = 'item'

	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
		# Read previous crawl data
		# file = open("auto.json", "r")
		# data = json.load(file)
		# pprint(data[0])
		# file.close()

		# file = open("auto.json", "w")
		# file.close()

		item = {}
		item['title'] = node.xpath('title/text()',).extract()
		item['link'] = node .xpath('link/text()',).extract()
		item['description'] = node.xpath('description/text()',).extract()
		item['title'][0] = item['title'][0].replace("\"","")
		item['source'] = "Báo Dân Trí"
		tab = response.url
		tab = tab.replace(".rss", "")
		tab = tab.replace("https://dantri.com.vn/", "")
		tab = tab.replace("-", " ")

		item['tab'] = tab
		item['date'] = node.xpath('pubDate/text()',).extract()

		# jdict = {'dict' : item}
		# with open('prev_data.json', 'w') as file:
		# 	file.write(json.dumps(item))
		# file.close()

		return item
