# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpaceXItem(scrapy.Item):
   	term = scrapy.Field()
   	location = scrapy.Field()
   	position = scrapy.Field()
   	department = scrapy.Field()
   	agency = scrapy.Field()
   	date = scrapy.Field()
   	link = scrapy.Field()
