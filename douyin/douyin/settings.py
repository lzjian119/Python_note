# -*- coding: utf-8 -*-

BOT_NAME = 'douyin'

SPIDER_MODULES = ['douyin.spiders']
NEWSPIDER_MODULE = 'douyin.spiders'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'zh-CN,zh;q=0.9',
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
}
#开启pipeline
ITEM_PIPELINES = {
    'douyin.pipelines.DouyinPipeline': 300,
}
IMAGES_STORE = 'E:\\douyin'
DOWNLOAD_DELAY = 1