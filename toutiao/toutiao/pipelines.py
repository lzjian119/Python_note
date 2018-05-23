# -*- coding: utf-8 -*-
import sys,os,urllib

class ToutiaoPipeline(object):
	def process_item(self, item, spider):
		dir_path = u'E:\\\\toutiao\\'+item['name']+"\\"
		isExists=os.path.exists(dir_path)
		#目录不存在则新建
		if not isExists:
			os.makedirs(dir_path) 
		name=dir_path+item['title']+'_'+item['count']+".mp4";
		#文件已存在提示"已下载"
		if  os.path.exists(name):
			#print "已下载"
			sys.exit()
		with  open(name,'wb') as file_writer:
			conn=urllib.urlopen(item['url'])
			file_writer.write(conn.read())
			file_writer.close()

