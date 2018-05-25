# -*- coding: utf-8 -*-
import sys,os,urllib

class DouyinPipeline(object):
	def process_item(self, item, spider):
		dir_path = u'E:\\\\douyin\\'+item['author']+"_"+item['uid']+"\\"
		isExists=os.path.exists(dir_path)
		#目录不存在则新建
		if not isExists:
			os.makedirs(dir_path) 
		name=dir_path+item['title']+".mp4";
		txt=dir_path+item['author']+"_"+item['uid']+".txt"

		#文件已存在提示"已下载"
		if  os.path.exists(name):
			print item['title']+"已下载"
		else:
			#print "正在下载"+item['title']+" ..."
			with  open(name,'wb') as file_writer:
				conn=urllib.urlopen(item['url'])
				file_writer.write(conn.read())
				file_writer.close()
			with  open(txt,'a+') as t:
				t.write(item['url']+"\n")
				file_writer.close()

