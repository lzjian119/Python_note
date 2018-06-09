# -*- coding: utf-8 -*-
import sys,os,urllib

class ToutiaoPipeline(object):
	def process_item(self, item, spider):
		dir_path = u'E:\\\\py\\mp4\\toutiao\\'+item['name']+"\\"
		isExists=os.path.exists(dir_path)
		#目录不存在则新建
		if not isExists:
			os.makedirs(dir_path) 
		name=dir_path+item['title']+'_'+item['definition']+".mp4"
		txt=dir_path+item['name']+"_播放统计.txt"
		#文件已存在提示"已下载"
		if  os.path.exists(name):
			print item['title']+"  已下载!"
			#sys.exit()
		else:
			with  open(name,'wb') as file_writer:
				conn=urllib.urlopen(item['url'])
				file_writer.write(conn.read())
				file_writer.close()
			with  open(txt,'a+') as t:
				t.write(item['title']+"  播放次数: "+item['count']+"\n")
				t.close()

