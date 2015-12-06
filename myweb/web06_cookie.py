#-*- coding:utf-8 -*-
import urllib2
import cookielib
import sys

type = sys.getfilesystemencoding()
# Cookie，指某些网站为了辨别用户身份、进行session跟
# 踪而储存在用户本地终端上的数据（通常经过加密）
# cookielib模块的主要作用是提供可存储cookie的对象，
# 以便于与urllib2模块配合使用来访问Internet资源。
# Cookielib模块非常强大，我们可以利用本模块的
# CookieJar类的对象来捕获cookie并在后续连接请求时
# 重新发送，比如可以实现模拟登录功能。该模块主要的
# 对象有CookieJar、FileCookieJar、MozillaCookieJar、
# LWPCookieJar。
# 它们的关系：CookieJar —-派生—->FileCookieJar  
# —-派生—–>MozillaCookieJar和LWPCookieJar
# 1）获取Cookie保存到变量
# 首先，我们先利用CookieJar对象实现获取cookie的功
# 能，存储到变量中，先来感受一下

# #声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2中的urlopen方法，也可以传入request
# reponse = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print 'Name = '+item.name
# 	print 'Value = '+item.value

# 2）保存Cookie到文件
# 在上面的方法中，我们将cookie保存到了cookie这个变量
# 中，如果我们想将cookie保存到文件中该怎么做呢？这时，
# 我们就要用到FileCookieJar这个对象了，在这里我们使
# 用它的子类MozillaCookieJar来实现Cookie的保存

# #设置保存cookie的文件
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后
#写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# ignore_discard: save even cookies set to be discarded. 
# ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
# 由此可见，ignore_discard的意思是即使cookies将被丢弃也将它
# 保存下来，ignore_expires的意思是如果在该文件中cookies已经
# 存在，则覆盖原文件写入，在这里，我们将这两个全部设置为True。

# 3）从文件中获取Cookie并访问
# 那么我们已经做到把Cookie保存到文件中了，如果以后想使用，可以
# 利用下面的方法来读取cookie并访问网站，感受一下

# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)
# req = urllib2.Request("http://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read().decode('utf-8').encode(type)