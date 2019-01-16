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
	name = 'mpi'
	allowed_domains = ["mpi.gov.vn"]
	start_urls = ['http://www.mpi.gov.vn/Pages/chuyenmuctin.aspx?idcm=188']
	def parse(self, response):
		names = response.xpath('//div[@class="myforumtext"]/table//tr/td/a/text()').extract()
		links = response.xpath('//div[@class="myforumtext"]/table//tr/td/a/@href').extract()
		descriptions = response.xpath('//div[@class="myforumtext"]/table//tr/td/text()').extract()
		dates = response.xpath('//div[@class="myforumtext"]/table//tr/td/a/span/text()').extract()

		de = []
		for x in range(len(descriptions)):
			descriptions[x] = descriptions[x].replace("\r\n                    ","")
			if len(descriptions[x]) >=30:
				de.append(descriptions[x])
				# print(descriptions[x])

		print(len(names))
		print(len(de))
		for x in range(len(names)):
			names[x] = names[x].replace("\r\n                        ","")
			# descriptions[x] = descriptions[x].replace("\r\n                        ","")
			yield {
			'title' : names[x],
			'link' : 'http://www.mpi.gov.vn/Pages/' + links[x],
			'description' : de[x],
			'date' : dates[x],
			'source' : 'Bộ Kế hoạch và Đầu tư'
			}
			# print(names[x])


		# tab1 = response.xpath('//li[@class="menu__cat-item"]/a/text()').extract()
