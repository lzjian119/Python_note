# -*- coding: utf-8 -*-
BOT_NAME = 'qiubai'
SPIDER_MODULES = ['qiubai.spiders']
NEWSPIDER_MODULE = 'qiubai.spiders'
DEFAULT_REQUEST_HEADERS = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
}