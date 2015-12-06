# -*- coding:utf-8 -*-
__author__ = 'lunabird'

import urllib
import urllib2
import re
import sys
import codecs

#处理页面标签类
class Tool:
	#去除img标签，7位长空格
	removeImg = re.compile('<img.*?>')
	#删除超链接标签
	removeAddr = re.compile('<a.*?>|</a>')
	#把换行的标签替换为\n
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	#将表格制表<td>替换为\t
	replaceTD = re.compile('<td>')
	#把段落开头替换为\n加两个空格
	replacePara = re.compile('<p.*?>')
	#把换行符和双换行符替换为\n
	replaceBR = re.compile('<br><br>|<br>')
	#将其余标签剔除
	removeExtraTag = re.compile('<.*?>')

	def replace(self, x):
		x = re.sub(self.removeImg, "", x)
		x = re.sub(self.removeAddr, "", x)
		x = re.sub(self.replaceLine, "\n", x)
		x = re.sub(self.replaceTD, "\t", x)
		x = re.sub(self.replacePara, "\n  ", x)
		x = re.sub(self.replaceBR, "\n", x)
		x = re.sub(self.removeExtraTag,"", x)
		#strip()将前后多余内容剔除
		return x.strip()
	



class BDTB:
	type = sys.getfilesystemencoding()
	
	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()

	
	def getPage(self, pageNum):
		
		try:
			url = self.baseUrl+self.seeLZ +'&pn='+str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			content = response.read()
			# print type
			# f = file('nba.txt', 'w+')
			# f.write(content)
			# f.close()
			return content
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "failed to connect baidutieba.",e.reason
				return None

	#get the title of the bbs
	def getTitle(self):
		# data = open("nba.txt").read()
		# # data = self.getPage(1).encode('utf-8')
		# if data[:3] == codecs.BOM_UTF8:
		# 	data = data[3:]
		# print data.decode("utf-8")
		page = self.getPage(1)
		pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
		result = re.search(pattern, page)
		if result:
			# print "bbs title:"+result.group(1)
			self.printToLog("bbs title:"+result.group(1))
			return result.group(1).strip()
		else:
			return None


	def getPageNum(self):
		# data = open("nba.txt").read()
		# if data[:3] == codecs.BOM_UTF8:
		# 	data = data[3:]
		# # print data.decode("utf-8")
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num".*?<span .*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result = re.search(pattern, page)
		if result:
			self.printToLog("page total num:"+result.group(1))
			return result.group(1).strip()
		else:
			return None

	def getContent(self,pageNum):
		# self.getPage(pageNum)
		page = self.getPage(pageNum)
		# if page[:3] == codecs.BOM_UTF8:
		# 	page = page[3:]
		
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>')
		items = re.findall(pattern, page)
		for item in items:
			# print item
			self.printToLog(self.tool.replace(item))

	def printToLog(self,mystr):
		f = open('txt/log.txt', 'a')
		f.write(mystr+"\n")
		f.close()

baseURL = 'http://tieba.baidu.com/p/4139773365'
bdtb = BDTB(baseURL,1)
bdtb.getTitle()
totalNum = int(bdtb.getPageNum())
for i in range(1, totalNum+1):
	bdtb.getContent(i)