# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
class Dbtop250Pipeline(object):
	def __init__(self):
		self.file = open('top250.txt', 'wb')
	def process_item(self, item, spider):
		content=''
		for i in item['name']:
			content += i+"\n"
		self.file.write(content)
		return item
		