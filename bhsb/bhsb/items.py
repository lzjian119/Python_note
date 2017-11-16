# -*- coding: utf-8 -*-
import scrapy
class BhsbItem(scrapy.Item):
	title = scrapy.Field()
	name = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()
	image_paths = scrapy.Field()
