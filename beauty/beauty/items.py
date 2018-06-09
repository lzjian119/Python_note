# -*- coding: utf-8 -*-
import scrapy
class BeautyItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	name = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()
	image_paths = scrapy.Field()
	date = scrapy.Field()