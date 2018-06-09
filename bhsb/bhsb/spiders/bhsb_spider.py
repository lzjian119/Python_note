# -*- coding: utf-8 -*-
import scrapy
from bhsb.items import BhsbItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class BhsbSpider(scrapy.spiders.Spider):
	name = "bhsb"
	allowed_domains = ["bh.sb"]
	start_urls = []
	# start_urls = [
		# "https://bh.sb/post/category/main/"	
	# ]
	for i in range(1,5):
		su="https://bh.sb/post/category/main/page/"+str(i)
		start_urls.append(su)

	def parse(self, response):		
		#获取当前页所有二级页面url
		data = response.body
		soup = BeautifulSoup(data, "lxml") 
		urls = response.xpath('//*[@class="excerpt excerpt-one"]/header/h2/a/@href').extract()
		for url in urls:
			yield scrapy.Request(url, callback=self.parse_content)
			
	
	#二级页面内容获取并保存到item	
	def parse_content(self, response):
		data = response.body
		soup = BeautifulSoup(data, "lxml") 
		item = BhsbItem()
		item['title'] = response.xpath('//head/title/text()').extract()[0].split(' ', 1 )[0]
		print item['title']
		item['name'] = response.xpath('//*[@class="article-content"]/p/text()').extract()
		item['image_urls'] = response.xpath('//*[@class="article-content"]/p/img/@src').extract()
		yield item

		

