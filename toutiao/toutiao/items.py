# -*- coding: utf-8 -*-
import scrapy
class ToutiaoItem(scrapy.Item):
	definition = scrapy.Field()
	title = scrapy.Field()
	url = scrapy.Field()
	name = scrapy.Field()
	count = scrapy.Field()

