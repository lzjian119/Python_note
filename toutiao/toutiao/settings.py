# -*- coding: utf-8 -*-

BOT_NAME = 'toutiao'

SPIDER_MODULES = ['toutiao.spiders']
NEWSPIDER_MODULE = 'toutiao.spiders'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
	'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
}
#开启pipeline
ITEM_PIPELINES = {
    'toutiao.pipelines.ToutiaoPipeline': 300,
}
IMAGES_STORE = 'E:\\toutiao'
DOWNLOAD_DELAY = 0.3