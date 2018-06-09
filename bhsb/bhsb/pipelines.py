# -*- coding: utf-8 -*-
import sys,os,urllib
class BhsbPipeline(object):
	def process_item(self, item, spider):
		dir_path = 'E:\\py\\bhsb\\'+item['title']+"\\"
		for i,img in enumerate(item['image_urls']):
			hou="."+str(img.split('.')[-1])
			isExists=os.path.exists(dir_path)
			if not isExists:
				os.makedirs(dir_path) 
			name=dir_path+item['name'][i].replace(u'\u200b','')+hou;
			if  os.path.exists(name):
				continue
			with  open(name,'wb') as file_writer:
				conn=urllib.urlopen(img)
				file_writer.write(conn.read())
			 	file_writer.close()
