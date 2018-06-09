# -*- coding: utf-8 -*-
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MyImagesPipeline(ImagesPipeline):
	def file_path(self, request, response=None, info=None):
		#通过上面的meta传递过来item
		item=request.meta['item']
		#通过上面的index传递过来列表中当前下载图片的下标		
		index=request.meta['index'] 
		#拼接文件名
		image_guid = str(index+1)+'.jpg'
		#下一句注释的为报错原本图片的名称
		#image_guid = request.url.split('/')[-1]
		#print "item=",item['name'][index],"\n index=",index
		#raw_input(' ') 
		#不按日期分目录
		#return '%s/%s' % (item['name'],image_guid)
		#按日期分目录
		path = item['date']+"\\"+item['name']
		return '%s/%s' % (path,image_guid)
		
		
	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield Request(image_url,meta={'item':item,'index':item['image_urls'].index(image_url)})

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		item['image_paths'] = image_paths
		return item

