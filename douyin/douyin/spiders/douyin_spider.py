# -*- coding: utf-8 -*-
import scrapy
from douyin.items import DouyinItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import re,sys,json,time,random,urlparse,os
import urllib,urllib2,requests,binascii,base64
from ..settings import DEFAULT_REQUEST_HEADERS
reload(sys)
sys.setdefaultencoding( "utf-8" )

def right_shift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n

uid="85757099860"
#uid="67176232618"
count="10"
dir_path = u'E:\\mp4\\douyin\\'
headers=DEFAULT_REQUEST_HEADERS

class DouyinSpider(scrapy.spiders.Spider):
	name = "douyin"

	allowed_domains = ["snssdk.com"]
	start_urls = [
		"https://www.amemv.com/aweme/v1/aweme/post/?user_id="+uid+"&max_cursor=0&count="+count
	]

	def parse(self, response):	
		item = DouyinItem()
		sites = json.loads(response.body_as_unicode()) 

		for site in sites['aweme_list']:  
			item['author']=site['author']['nickname']
			item['uid']=uid
			item['title']=site['desc']
			item['count']=str(site['statistics']['play_count'])
			#获取跳转后的url
			url=site['video']['play_addr']['url_list'][0]
			r = requests.head(url, stream=True,headers=headers)
			if r.status_code == 404:
				continue
			else:
				item['url']=r.headers['Location']
			yield item
		cmd	= "explorer "+dir_path
		os.system(cmd)
		




