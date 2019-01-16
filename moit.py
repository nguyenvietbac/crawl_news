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
	name = 'moit'
	allowed_domains = ["moit.gov.vn"]
	start_urls = ['http://www.moit.gov.vn/web/guest/thoi-su']
	def parse(self, response):
		# name = response.xpath('//section[@class="category-list"]/div[@class="media-list"]//div[@class="media-body article-info"]/a/text()').extract()
		names = response.xpath('//section[@class="category-list"]/div/article/div[@class="media-body article-info"]/a/text()').extract()
		links = response.xpath('//section[@class="category-list"]/div/article/div[@class="media-body article-info"]/a/@href').extract()
		dates = response.xpath('//section[@class="category-list"]/div/article/div[@class="media-body article-info"]/p[@class="more-info"]/text()').extract()
		descriptions = response.xpath('//section[@class="category-list"]/div/article/div[@class="media-body article-info"]/p[@class="description"]/text()').extract()
		print(len(names))
		print(len(links))

		for x in range(len(names)):
			yield {
			'title' : names[x],
			'link' : links[x],
			'description' : descriptions[x],
			'date' : dates[x],
			'source' : "Bộ Công Thương",
			}

		# tab1 = response.xpath('//li[@class="menu__cat-item"]/a/text()').extract()
