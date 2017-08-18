# -*- coding: utf-8 -*-
import scrapy

class Dbtop250Item(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	name = scrapy.Field()