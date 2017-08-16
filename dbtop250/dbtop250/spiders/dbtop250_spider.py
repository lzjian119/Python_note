# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from dbtop250.items import Dbtop250Item

class Dbtop250Spider(BaseSpider):
	name = "dbtop250"
	allowed_domains = ["douban.com"]
	start_urls = [
		"https://movie.douban.com/top250",
	]
	print "test测试开始----\n".decode('utf-8')
	def parse(self, response):
		item = Dbtop250Item()
		item['title'] = response.xpath('//head/title/text()').extract()[0]
		item['name'] = response.xpath('//span[@class="title"][1]/text()').extract()
		item['link'] = response.xpath('//span[@class="next"]/a/@href').extract()
		#print item['title']
		yield item
		if item['link']:
			#raw_input(' ') 	#暂停键
			next_page = "https://movie.douban.com/top250"+item['link'][0]
			#print 'next=',next_page
			yield scrapy.Request(next_page, callback=self.parse)
	print "test测试结束----\n".decode('utf-8')