# -*- coding: utf-8 -*-

BOT_NAME = 'beauty'

SPIDER_MODULES = ['beauty.spiders']
NEWSPIDER_MODULE = 'beauty.spiders'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {						'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
	'beauty.middlewares.ProxyMiddleware': 100,
}

DEFAULT_REQUEST_HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/jpg,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
}
#开启pipeline
ITEM_PIPELINES = {
    'beauty.pipelines.MyImagesPipeline': 300,
}
IMAGES_STORE = 'E:\\py\\beauty'
DOWNLOAD_DELAY = 0.5