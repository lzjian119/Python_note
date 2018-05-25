# -*- coding: utf-8 -*-
import scrapy
from douyin.items import DouyinItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import re,sys,json,time,random,urlparse,requests,binascii,base64
import urllib
reload(sys)
sys.setdefaultencoding( "utf-8" )

def right_shift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n

uid="85757099860"
#uid="67176232618"
count="20"

class DouyinSpider(scrapy.spiders.Spider):
	name = "douyin"

	allowed_domains = ["amemv.com"]
	start_urls = [
		"https://www.amemv.com/aweme/v1/aweme/post/?user_id="+uid+"&max_cursor=0&count="+count
	]

	def parse(self, response):	
		item = DouyinItem()
		sites = json.loads(response.body_as_unicode()) 
		
		for site in sites['aweme_list']:  
			#u = "https://www.365yg.com/a"+str(site['group_id'])+"#mid="+uid
			item['author']=site['author']['nickname']
			item['uid']=uid
			item['title']=site['desc']
			item['url']=site['video']['play_addr']['url_list'][0]
			item['count']=site['statistics']['play_count']
			yield item


