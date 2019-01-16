import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import pymongo
import datetime

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Dulieu_adaroi"]
# mycol = mydb["Price"]

class AutoSpider(CrawlSpider):
	download_delay = 0.5
	download_timeout = 30
	name = 'mof'
	allowed_domains = ["mof.gov.vn"]
	start_urls = ['http://www.mof.gov.vn/']
	def parse(self, response):
		link = 'http://www.mof.gov.vn/'
		request = scrapy.Request(response.urljoin(link), self.parse_mof, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': {'wait': 5.5}
			}
		})
		# request.meta['tab'] = tab
		# request.meta['item'] = link
		yield request
	def parse_mof(self, response):
		names = response.xpath('//div[@class="image_thumb"]/ul/li/div/a/text()').extract()
		links = response.xpath('//div[@class="image_thumb"]/ul/li/div/a/@href').extract()
		dates = response.xpath('//div[@class="image_thumb"]/ul/li/div/span/text()').extract()
		print(len(links))
		print(len(names))
		print(len(dates))

		if names == [] or links == [] or dates == []:
			link = 'http://www.mof.gov.vn/'
			request = scrapy.Request(response.urljoin(link), self.parse_mof, meta={
				'splash': {
					'endpoint': 'render.html',
					'args': {'wait': 5.5}
				}
			})
			yield request
		else :
			for x in range(len(names)):
				yield {
				'title' : names[x],
				'link' : "http://www.mof.gov.vn" + links[x],
				'description' : "",
				'date' : dates[x],
				'source' : "Bộ Tài chính",
				}
