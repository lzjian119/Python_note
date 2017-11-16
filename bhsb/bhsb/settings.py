# -*- coding: utf-8 -*-

BOT_NAME = 'bhsb'

SPIDER_MODULES = ['bhsb.spiders']
NEWSPIDER_MODULE = 'bhsb.spiders'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/jpg,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
}
#开启pipeline
ITEM_PIPELINES = {
    'bhsb.pipelines.BhsbPipeline': 300,
}
IMAGES_STORE = 'E:\\bhsb'
DOWNLOAD_DELAY = 0.3