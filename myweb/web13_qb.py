# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys

type = sys.getfilesystemencoding()

# page = 1
# url = 'http://www.qiushibaike.com/hot/page/'+str(page)
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
# headers = {'User-Agent' : user_agent}
# try:
# 	request = urllib2.Request(url,headers = headers)
# 	response = urllib2.urlopen(request)
# 	# print response.read().decode('utf-8').encode(type)
# except urllib2.URLError, e:
# 	if hasattr(e, "code"):
# 		print e.code
# 	if hasattr(e,"reason"):
# 		print e.reason

# content = response.read().decode('utf-8')
# pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
# items = re.findall(pattern, content)
# for item in items:
# 	print item[0], item[1], item[2], item[3], item[4]

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

f = file('qb.html','w+')

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    print items
    # f.write(content.encode(type))
    # f.close()
    # print content
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
# 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示
# 使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大
# 量用到 .*? 的搭配。

# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面
# 的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代
# 表第二个(.*?)所指代的内容，以此类推。

# 3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。