# coding: GBK
import scrapy
from beauty.items import BeautyItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import re,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class BeautySpider(scrapy.spiders.Spider):
	name = "beauty"
	allowed_domains = ["t66y.com"]
	start_urls = [
		"http://t66y.com/thread0806.php?fid=8"
	]

	def parse(self, response):	
		#获取当前页所有二级页面url
		data = response.body
		soup = BeautifulSoup(data, "lxml") 
		urls = soup.find_all(string=re.compile(u"\[寫真"))
		
		for url in urls:
			#for循环获取二级页面的内容(调用parse_content方法)
			u = "http://t66y.com/"+url.parent.h3.a['href']
			yield scrapy.Request(u, callback=self.parse_content)
		
		#获取完所有二级页面内容后，跳转到下一页
		next_page = "http://t66y.com/"+soup.find(string=re.compile(u"下一頁")).parent['href']
		if next_page:
			yield scrapy.Request(next_page, callback=self.parse)
		
	#二级页面内容获取并保存到item	
	def parse_content(self, response):
		item = BeautyItem()
		item['title'] = response.xpath('//head/title/text()').extract()[0]
		item['name'] =  response.xpath('//h4/text()').extract()[0]
		image_urls1 = response.xpath('//*[@class="tpc_content do_not_catch"]/input/@src').extract()
		image_urls2 = response.xpath('//*[@class="tpc_content do_not_catch"]/input/@data-src').extract()
		
		#item['image_urls'] = response.xpath('//*[@class="tpc_content do_not_catch"]/input/@data-src').extract()
		item['image_urls'] = image_urls1 + image_urls2
		date = response.xpath('//*[@class="tipad"]/text()').extract()
		item['date']=date[1].split(' ', 1 )[0].split(':', 1 )[1]
		yield item
	
		

