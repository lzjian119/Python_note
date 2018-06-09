# -*- coding: utf-8 -*-
import scrapy
from toutiao.items import ToutiaoItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup  
import os,re,sys,json,time,random,urlparse,requests,binascii,base64

reload(sys)
sys.setdefaultencoding( "utf-8" )

def right_shift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n

uid="58986695909"
count="10"
dir_path = u'E:\\mp4\\toutiao\\'

class ToutiaoSpider(scrapy.spiders.Spider):
	name = "toutiao"

	allowed_domains = ["365yg.com"]
	start_urls = [
		"http://www.365yg.com/c/user/article/?user_id="+uid+"&count="+count
		#"http://www.365yg.com/a6558340435675185667/#mid="+uid

	]

	def parse(self, response):	
		''' '''
		sites = json.loads(response.body_as_unicode()) 
		for site in sites['data']:  
			u = "https://www.365yg.com/a"+site['group_id']+"#mid="+uid
			yield scrapy.Request(u,callback=self.parse_content)
				
	#二级页面内容获取并保存到item		
	def parse_content(self,response):
		''' '''
		item = ToutiaoItem()
		data = response.body
		soup = BeautifulSoup(data, "lxml") 	
		#获取视频Id,作者,播放次数
		t = soup.find(text=re.compile("videoId"))

		vid=re.findall(r'videoId: \'(.*)\'',str(t))[0]
		item['name']=re.findall(r'name: \'(.*)\'',str(t))[0]
		item['count']=re.findall(r'videoPlayCount: (.*)\,',str(t))[0]

		#生成获取视频地址的api地址
		r = str(random.random())[2:]
		url="http://ib.365yg.com/video/urls/v/1/toutiao/mp4/%s" % vid
		n = urlparse.urlparse(url).path + '?r=' + r
		c = binascii.crc32(n)
		s = right_shift(c, 0)
		#获取视频下载地址及相关信息
		res = requests.get(url + '?r=%s&s=%s' % (r, s))
		video_list = res.json()['data']['video_list']
		num='%s%s'%('video_',str(res.json()['total']))

		item['title'] = response.xpath('//head/title/text()').extract()[0]
		item['definition']=video_list[num]['definition']
		main_url=video_list[num]['main_url']
		item['url']=base64.standard_b64decode(main_url)
		#for i in item:
		#	print i,item[i]
		yield item
	