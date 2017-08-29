# -*- coding: utf-8 -*-
import scrapy,sys
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor  
from bs4 import BeautifulSoup  

class QiubaiSpider(scrapy.spiders.Spider):
	name = "qiubai"
	allowed_domains = ["qiushibaike.com"]
	start_urls = [
		"http://www.qiushibaike.com/hot/page/",
	]	
	def parse(self, response):
		print "\n开始载入糗百段子(按q退出):\n".decode('utf-8')
		data = response.body
		soup = BeautifulSoup(data, "lxml") 
		contents = soup.find_all("div","article")	
		#获取每条段子的内容、作者和点赞数
		for content in contents:
			cont = content.span.get_text().encode("GBK", "ignore");
			auth = content.h2.get_text().replace("\n","").encode("GBK", "ignore");
			num = content.i.get_text().replace("\n","").encode("GBK", "ignore");
			print "作者:".decode('utf-8'),auth,"\t点赞数:".decode('utf-8'),num,
			print cont,"-"*40
			input = raw_input(' ') 
			if input == "q" or input == "Q" :
				sys.exit()		
		#爬取下一页内容
		next_page = 'http://qiushibaike.com'+soup.find("span",'next').parent['href']
		#print "next_url:",next_page
		yield scrapy.Request(next_page, callback=self.parse)
		
		