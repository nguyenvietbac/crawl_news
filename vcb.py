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
	name = 'vcb'
	allowed_domains = ["vietcombank.com.vn"]
	start_urls = ['https://www.vietcombank.com.vn/']
	def parse(self, response):
		names = response.xpath('//ul[@class="news-list"]/li/a/text()').extract()
		links = response.xpath('//ul[@class="news-list"]/li/a/@href').extract()
		dates = response.xpath('//ul[@class="news-list"]/li/i/text()').extract()

		for x in range(len(names)):
			yield{
			'title' : names[x],
			'link' : 'https://www.vietcombank.com.vn/' + links[x],
			'date' : dates[x],
			'source' : 'Vietcombank',
			'description' : '',
			}		
