import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'vne'
	allowed_domains = ["vneconomy.vn"]
	start_urls = ['http://vneconomy.vn/rss/doanh-nhan.rss',
				"http://vneconomy.vn/rss/doanh-nhan.rss",
				"http://vneconomy.vn/rss/tai-chinh.rss",
				"http://vneconomy.vn/rss/chung-khoan.rss",
				"http://vneconomy.vn/rss/thi-truong.rss",
				"http://vneconomy.vn/rss/bat-dong-san.rss",
				"http://vneconomy.vn/rss/the-gioi.rss",
				"http://vneconomy.vn/rss/cuoc-song-so.rss",
				"http://vneconomy.vn/rss/xe-360.rss"]
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
		item['source'] = 'vneconomy.vn'
		tab = response.url
		tab = tab.replace(".rss", "")
		tab = tab.replace("http://vneconomy.vn/rss/", "")
		tab = tab.replace("-", " ")

		item['tab'] = tab		
		item['date'] = node.xpath('pubDate/text()',).extract()
		# jdict = {'dict' : item}
		# with open('prev_data.json', 'w') as file:
		# 	file.write(json.dumps(item))
		# file.close()

		return item
		# le = len(data)
		# count = 0
		# for x in range(le):
		# 	if item == data[x]:
		# 		continue
		# 	count += 1

		# if count == le:
		# 	return item



		