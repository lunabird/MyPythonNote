# -*- coding : utf-8 -*-
import urllib
import urllib2
import re


class imgTest:

	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		# self.tool = Tool()
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
	#get img urls		
	def getAllImageURLs(self,pageNum):
		page = self.getPage(pageNum)		
		patternImg = re.compile(r'<img class="BDE_Image" pic_type="0".*?src="(.+?\.jpg)" pic_ext="jpeg"')
		images = re.findall(patternImg, page)
		for item in images:
			print item
			self.printToLog("".join(item))
			# print("\n\n")
		return images
	#print to log.txt
	def printToLog(self,mystr):
		f = open('txt/log.txt', 'a')
		# f = open('txt/log.txt')
		f.write(mystr+"\n")
		f.close()

	#get the title of the bbs
	def getTitle(self):
		page = self.getPage(1)
		pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
		result = re.search(pattern, page)
		if result:
			self.printToLog("bbs title:"+result.group(1))
			return result.group(1).strip()
		else:
			return None
	#get the total number of the tiezi
	def getPageNum(self):
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num".*?<span .*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result = re.search(pattern, page)
		if result:
			self.printToLog("page total num:"+result.group(1))
			return result.group(1).strip()
		else:
			return None
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

baseURL = 'http://tieba.baidu.com/p/3925387672'
imgtest = imgTest(baseURL,1)
totalnum = int(imgtest.getPageNum())

imageCount = 0
for i in range(1, totalnum+1):
	imageURLs = imgtest.getAllImageURLs(i)
	imgtest.saveImgs(imageURLs,"pic",imageCount)
	imageCount += len(imageURLs)
	print imageCount

# imageURLs = imgtest.getAllImageURLs(2)
# imageCount = 0
# imageCount += len(imageURLs)
# print imageCount

# imgtest.saveImg('http://imgsrc.baidu.com/forum/w%3D580/sign=850c0142bf014a90813e46b599763971/713452da81cb39db2de6d9a6d6160924aa183008.jpg', 'pic\lbj.jpg')

# imageURL = 'http://imgsrc.baidu.com/forum/w%3D580/sign=850c0142bf014a90813e46b599763971/713452da81cb39db2de6d9a6d6160924aa183008.jpg'
# splitPath = imageURL.split('.')
# fTail = splitPath.pop()
# print fTail


