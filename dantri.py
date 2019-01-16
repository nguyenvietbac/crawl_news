import scrapy
from scrapy.spiders import XMLFeedSpider
import json
from pprint import pprint


# from news.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'dantri'
	allowed_domains = ["dantri.com.vn"]
	start_urls = ['https://dantri.com.vn/trangchu.rss',
				"https://dantri.com.vn/suc-khoe.rss",
				"https://dantri.com.vn/xa-hoi.rss",
				"https://dantri.com.vn/giai-tri.rss",
				"https://dantri.com.vn/giao-duc-khuyen-hoc.rss",
				"https://dantri.com.vn/the-thao.rss",
				"https://dantri.com.vn/the-gioi.rss",
				"https://dantri.com.vn/kinh-doanh.rss",
				"https://dantri.com.vn/o-to-xe-may.rss",
				"https://dantri.com.vn/suc-manh-so.rss",
				"https://dantri.com.vn/tinh-yeu-gioi-tinh.rss",
				"https://dantri.com.vn/chuyen-la.rss",
				"https://dantri.com.vn/viec-lam.rss",
				"https://dantri.com.vn/nhip-song-tre.rss",
				"https://dantri.com.vn/tam-long-nhan-ai.rss",
				"https://dantri.com.vn/phap-luat.rss",
				"https://dantri.com.vn/ban-doc.rss",
				"https://dantri.com.vn/dien-dan.rss",
				"https://dantri.com.vn/tuyen-sinh.rss",
				"https://dantri.com.vn/blog.rss",
				"https://dantri.com.vn/van-hoa.rss",
				"https://dantri.com.vn/du-hoc.rss",
				"https://dantri.com.vn/du-lich.rss",
				"https://dantri.com.vn/doi-song.rss",
				"https://dantri.com.vn/khoa-hoc-cong-nghe.rss",
				"https://dantri.com.vn/sea-games-28.rss",
				"https://dantri.com.vn/bat-dong-san.rss"
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
		# le = len(data)
		# count = 0
		# for x in range(le):
		# 	if item == data[x]:
		# 		continue
		# 	count += 1

		# if count == le:
		# 	return item



		