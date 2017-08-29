# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from dbtop250.items import Dbtop250Item

class Dbtop250Spider(Spider):
	name = "dbtop250"
	allowed_domains = ["douban.com"]
	start_urls = [
		"https://movie.douban.com/top250",
	]
	def parse(self, response):
		item = Dbtop250Item()
		item['title'] = response.xpath('//head/title/text()').extract()[0]
		item['name'] = response.xpath('//span[@class="title"][1]/text()').extract()
		item['link'] = response.xpath('//span[@class="next"]/a/@href').extract()
		yield item
		if item['link']:
			next_page = "https://movie.douban.com/top250"+item['link'][0]
			yield scrapy.Request(next_page, callback=self.parse)
