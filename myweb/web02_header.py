# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys

type = sys.getfilesystemencoding()


url = 'http://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'  
values = {'username' : 'lunabird@163.com',  'password' : 'huangpeng123' }  
headers = { 'User-Agent' : user_agent ,
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Host' : 'www.zhihu.com',
			'Referer':'http://www.zhihu.com'}  
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read().decode('utf-8').encode(type)