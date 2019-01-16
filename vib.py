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
	name = 'vib'
	allowed_domains = ["vib.com.vn"]
	start_urls = ['https://vib.com.vn/wps/portal?1dmy&page=news.landing&urile=wcm:path:/vib-vevib-vn/sa-news/vib-news/vib-news']
	def parse(self, response):
		# names = response.xpath('//div[@id="newslandingbound"]/div/div/div/a[1]/text()').extract()
		# print(names)

		link = response.url
		request = scrapy.Request(response.urljoin(link), self.parse_vib, meta={
			'splash': {
				'endpoint': 'render.html',
				'args': {'wait': 5.5}
			}
		})
		# request.meta['tab'] = tab
		# request.meta['item'] = link
		yield request

	def parse_vib(self,response):

		# names = response.xpath('//div[@id="newshomepage"]/div[@class="accordion-content"]/ul/li/a/text()').extract()
		# links = response.xpath('//div[@id="newshomepage"]/div[@class="accordion-content"]/ul/li/a/@href').extract()
		# print(len(names))
		# print(len(links))
		print("names")
		# names = response.xpath('//div[@id="newslandingbound"]/div/div/div/a[1]/text()').extract()
		# links = response.xpath('//div[@id="newslandingbound"]/div/div/a/@href').extract()
		# dates = response.xpath('//div[@id="newslandingbound"]/div/div/div/small/text()').extract()
		# print(len(names))
		# print(len(links))

		# for x in date:
		# 	print(x)

		names = response.xpath('//div[@id="vib-v2-news-list-load-ajax"]/div/div/a/text()').extract()
		print(names)
		# for x in range(len(names)):
			

		# 	yield{
		# 	'title' : names[x],
		# 	'link' : 'https://vib.com.vn' + links[x],
		# 	'date' : dates[x],
		# 	'source' : 'VIB Bank',
		# 	'description' : '',
		# 	}


