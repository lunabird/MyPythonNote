# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys
type = sys.getfilesystemencoding()


# 1.URLError
# 首先解释下URLError可能产生的原因：
# 网络无连接，即本机无法上网
# 连接不到特定的服务器
# 服务器不存在
# 在代码中，我们需要用try-except语句来包围并捕获相应的异常。
# 下面是一个例子，先感受下它的风骚

# requset = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(requset)
# except urllib2.URLError, e:
#     print e.reason
# 我们利用了 urlopen方法访问了一个不存在的网址，运行结果如下：
# [Errno 11004] getaddrinfo failed
# 它说明了错误代号是11004，错误原因是 getaddrinfo failed

# 2.HTTPError
# HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，
# 服务器上都会对应一个应答对象response，其中它包含一个数字”状态
# 码”。举个例子，假如response是一个”重定向”，需定位到别的地址获取
# 文档，urllib2将对此进行处理。
# 其他不能处理的，urlopen会产生一个HTTPError，对应相应的状态吗，
# HTTP状态码表示HTTP协议所返回的响应的状态。

# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
#     response = urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.code
#     print e.reason

# HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常
# 的后面，如果子类捕获不到，那么可以捕获父类的异常，所以上述的代码可以
# 这么改写
# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
# 	urllib2.urlopen(req)
# except urllib2.HTTPError, e:
# 	print e.code
# except urllib2.URLError, e:
# 	print e.reason
# else:
# 	print "OK"


# 另外还可以加入 hasattr属性提前对属性进行判断，代码改写如下
req = urllib2.Request('http://www.baidu.com')
try:
	urllib2.urlopen(req)
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
else:
	print "OK"
