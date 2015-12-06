# -*- coding:utf-8 -*-
import urllib
import urllib2
import sys
# urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
# 假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，
# 它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔
# 一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！

type = sys.getfilesystemencoding()


enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)