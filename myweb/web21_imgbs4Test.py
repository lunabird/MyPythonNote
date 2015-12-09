# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib
import re

class imgTest:

	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)

	#print to log.txt
	def printToLog(self,mystr):
		f = open('txt/log.txt', 'a')
		f.write(mystr+"\n")
		f.close()
	#get the html source code
	def getPage(self, pageNum):
		try:
			url = self.baseUrl+self.seeLZ +'&pn='+str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			content = response.read()
			return content
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "failed to connect baidutieba.",e.reason
				return None

	def getPageNum(self):
		page = self.getPage(1)
		soup = BeautifulSoup(page,'html.parser')
		pageNum = soup.find_all("span",class_='red')[1].string
		return pageNum

	def getTitle(self):
		page = self.getPage(1)
		soup = BeautifulSoup(page,'html.parser')
		return soup.h3.string

	def getAllImageURLs(self,pageNum):
		page = self.getPage(pageNum)	
		soup = BeautifulSoup(page,'html.parser')	
		imgTags = soup.find_all("img",class_="BDE_Image")
		imgURLs = []
		for item in imgTags:
			imgURLs.append(item.get('src'))
		print imgURLs
		self.printToLog(','.join(imgURLs))
		return imgURLs
	#save a single img 
	def saveImg(self,imageURL,filename):
		u = urllib.urlopen(imageURL)
		data = u.read()
		f = open(filename,'wb')
		f.write(data)
		f.close()
	#download images
	def saveImgs(self, images, name, num):
		number = num
		for imageURL in images:
			splitPath = imageURL.split('.')
			fTail = splitPath.pop()
			if len(fTail)>3:
				fTail = "jpg"
			fileName = name+"/"+str(number)+"."+fTail
			self.saveImg(imageURL,fileName)
			number += 1


baseURL = 'http://tieba.baidu.com/p/3760562085'
imgtest = imgTest(baseURL,1)
totalnum = int(imgtest.getPageNum())

imageCount = 0
for i in range(1, totalnum+1):
	imageURLs = imgtest.getAllImageURLs(i)
	imgtest.saveImgs(imageURLs,"pic",imageCount)
	imageCount += len(imageURLs)
	print imageCount

# page = imgtest.getPage(1)
# soup = BeautifulSoup(page,'html.parser')
# print soup.find_all("span",class_='red')[1].string
# print soup.find_all(re.compile("^<span class='red'>.</span>$"))
# <li class="l_reply_num" style="margin-left:8px"><span class="red" style="margin-right:3px">217</span>回复贴，共<span class="red">8</span>页</li>
# print soup.find_all(text="8")
# printToLog(soup.prettify())
# print soup.find_all("li",class_="l_reply_num")
# print soup.head.title
# print soup.h3.string

# imgTags = soup.find_all("img",class_="BDE_Image")
# for item in imgTags:
# 	print item.get('src')
	# isoup = BeautifulSoup(item, 'html.parser')
	# print isoup.img.get('src')
	# print "\n\n"