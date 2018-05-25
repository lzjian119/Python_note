# -*- coding: utf-8 -*-
import scrapy
class DouyinItem(scrapy.Item):
	author = scrapy.Field()
	uid = scrapy.Field()
	title = scrapy.Field()
	url = scrapy.Field()
	count = scrapy.Field()


