import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime


class AutoSpider(CrawlSpider):
	download_delay = 0.5
	download_timeout = 30
	name = 'ce'
	allowed_domains = ["finance.ce.cn"]
	start_urls = ['http://finance.ce.cn/']
	def parse(self, response):
		tab_spotline = response.xpath('//div[@class="w_650"]/div[@class="tit"]/h3/text()').extract()
		links = response.xpath('//div[@class="w_650"]/div[@class="pictxt1"]/div[@class="txt1"]/h4/a/@href').extract()
		names = response.xpath('//div[@class="w_650"]/div[@class="pictxt1"]/div[@class="txt1"]/h4/a/text()').extract()
		description = response.xpath('//div[@class="w_650"]/div[@class="pictxt1"]/div[@class="txt1"]/p/text()').extract()
		# print(links)
		# print(names)
		# print(description)
		# print(len(links))
		# print(len(names))
		# print(len(description))	
		date = datetime.datetime.now().date()
		date = str(date)
		if len(links) == len(names):
			for x in range(len(names)):
				yield{
					'title' : names[x],
					'description' : description[x],
					'link' : links[x],
					'tab' : tab_spotline,
					'date' : date,
					'source' : 'China Economic News',
				}

		tabs = response.xpath('//div[@class="w_650"]/div[@class="tit1"]/h3/text()').extract()
		for x in range(len(tabs)):
			links = response.xpath('//div[@class="w_650"]/div[@class="list1"][$o]/ul/li/a/@href',o = x + 1).extract()
			titles = response.xpath('//div[@class="w_650"]/div[@class="list1"][$o]/ul/li/a/text()',o = x + 1).extract()
			dates = response.xpath('//div[@class="w_650"]/div[@class="list1"][$o]/ul/li/span/text()',o = x + 1).extract()
			print(len(links))
			print(len(titles))
			print(len(dates))
			if len(links) == len(titles):
				for y in range(len(titles)):
					links[y] = links[y].replace("./", "http://finance.ce.cn/")
					yield{
						'title' : titles[y],
						'description' : '',
						'link' : links[y],
						'tab' : tabs[x],
						'date' : dates[y],
						'source' : 'China Economic News'
					}

