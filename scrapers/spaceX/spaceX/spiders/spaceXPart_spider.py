import scrapy
from scrapy.contrib.spiders import CrawlSpider
from spaceX.items import SpaceXItem
import datetime


class spaceXPartSpider(CrawlSpider):
	name = 'spaceXPart'
	allowed_domains = ["spacex.com"]
	start_urls = ["http://www.spacex.com/careers/list?type%5B%5D=53"]

	def parse(self, response):
		for url in response.xpath('//a/@href').extract():
			if '/careers/position/' in url:
				url = u'http://www.spacex.com' + url
				yield scrapy.Request(url, callback=self.parse_job)

	def parse_job(self, response):
		print('parsing job %s' % response.url + '\n')
		
		item = SpaceXItem()
		item['term'] = 'Part-time'
		item['location'] = [s.encode('utf-8') for s in response.xpath('//div[@class="field field-name-field-job-location field-type-taxonomy-term-reference field-label-above"]/a[@href]/text()').extract()][0]
		item['position'] = [r.encode('utf-8') for r in response.xpath('//div[@class="quick-info"]/h2[@class="position-title"]/text()').extract()][0]
		item['link'] = [t.encode('utf-8') for t in response.xpath('//div[@class="apply-now"]/div[@class="apply-button"]/a[@class="callout apply-now"]/@href').extract()][0]
		
		dept = [z.encode('utf-8') for z in response.xpath('//div[@class="department-info"]/text()').extract()]
		dept = dept[0].strip("\n")
		dept = dept.strip()
		item['department'] = dept
		item['agency'] = 'SpaceX'

		date = datetime.date.today()
		item['date'] = date.strftime('%m-%d-%Y')

		return item
		# print(item)
