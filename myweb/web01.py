# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys

type = sys.getfilesystemencoding()
# print mystr.decode('utf-8').encode(type)



# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()


#urlopen(url, data, timeout)  是默认的访问方式
#第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

#通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确。
# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values) #urlencode方法将字典编码，命名为data
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read().decode('utf-8').encode(type)

# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.urlencode(values) 
# url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read().decode('utf-8').encode(type)



# GET方式：
# 至于GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可。

values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read().decode('utf-8').encode(type)