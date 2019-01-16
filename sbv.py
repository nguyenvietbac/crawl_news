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
	name = 'sbv'
	allowed_domains = ["sbv.gov.vn"]
	start_urls = ['https://www.sbv.gov.vn/']
	def parse(self, response):
		# names = response.xpath('//div[@class="myforumtext"]/table//tr/td/a/text()').extract()
		link = 'https://www.sbv.gov.vn/'
		request = scrapy.Request(response.urljoin(link), self.parse_sbv, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': {'wait': 10.5}
			}
		})
		# request.meta['tab'] = tab
		# request.meta['item'] = link
		yield request

	def parse_sbv(self, response):
		names = response.xpath('//tbody/tr/td/div/a/text()').extract()
		links = response.xpath('//tbody/tr/td/div/a/@href').extract()
		dates = response.xpath('//tbody/tr/td/div/div/text()').extract()
		# print(len(links))
		# print(len(names))

		
		if names == [] or links == [] or dates == []:
			link = 'https://www.sbv.gov.vn/'
			request = scrapy.Request(response.urljoin(link), self.parse_sbv, meta={
				'splash': {
					'endpoint': 'render.html',
					'args': {'wait': 10.5}
				}
			})
			yield request
		else :
			for x in range(len(names)):
				yield {
				'title' : names[x],
				'link' : "https://www.sbv.gov.vn" + links[x],
				'description' : "",
				'date' : dates[x],
				'source' : "Ngân hàng Nhà nước",
				}
