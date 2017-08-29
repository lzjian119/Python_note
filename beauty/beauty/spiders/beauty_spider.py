# coding: GBK
import scrapy
from beauty.items import BeautyItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import re

class BeautySpider(scrapy.spiders.Spider):
	name = "beauty"
	allowed_domains = ["t66y.com"]
	start_urls = [
		"http://t66y.com/thread0806.php?fid=8"
	]

	def parse(self, response):	
		#��ȡ��ǰҳ���ж���ҳ��url
		data = response.body
		soup = BeautifulSoup(data, "lxml") 
		urls = soup.find_all(string=re.compile(u"\[����"))
		
		for url in urls:
			#forѭ����ȡ����ҳ�������(����parse_content����)
			u = "http://t66y.com/"+url.parent.h3.a['href']
			yield scrapy.Request(u, callback=self.parse_content)
		
		#��ȡ�����ж���ҳ�����ݺ���ת����һҳ
		next_page = "http://t66y.com/"+soup.find(string=re.compile(u"��һ�")).parent['href']
		if next_page:
			yield scrapy.Request(next_page, callback=self.parse)
		
	#����ҳ�����ݻ�ȡ�����浽item	
	def parse_content(self, response):
		item = BeautyItem()
		item['title'] = response.xpath('//head/title/text()').extract()[0]
		item['name'] =  response.xpath('//h4/text()').extract()[0]
		item['image_urls'] = response.xpath('//*[@class="tpc_content do_not_catch"]/input/@src').extract()
		yield item
	
		

