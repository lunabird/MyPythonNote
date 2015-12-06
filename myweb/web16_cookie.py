# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re

def printToLog(mystr):
		f = open('login.txt', 'a')
		f.write(mystr+"\n")
		f.close()


auth_url = 'http://www.nowamagic.net/'
home_url = 'http://www.nowamagic.net/librarys/accounts/profile/'

#登录用户名和密码
data = {
	'username':'lunabird@163.com',
	'password':'huangpeng123'
}
#urllib进行编码
post_data = urllib.urlencode(data)
#发送header
headers = {
	'Host':'www.nowamagic.net',
	'Refer':'http://www.nowamagic.net'
}
# #初始化一个cookieJar来处理cookie
# cookieJar = cookielib.CookieJar()
# #实例化一个全局opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# #获取cookie
# req = urllib2.Request(auth_url,post_data,headers)
# #result = opener.open(req)
req = urllib2.Request(auth_url, post_data, headers) 
req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')

ckjar = cookielib.MozillaCookieJar('mycookie.txt') 
ckproc = urllib2.HTTPCookieProcessor(ckjar)
opener = urllib2.build_opener(ckproc)
f = opener.open(req) 
htm = f.read() 
f.close()
ckjar.save(ignore_discard=True, ignore_expires=True)


# #访问主页 自动带着cookie信息
# result = opener.open(home_url)
# #显示结果
# printToLog(result.read())