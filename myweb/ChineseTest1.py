#coding=gbk
import codecs
data = open("test.txt").read()
if data[:3] == codecs.BOM_UTF8:
	data = data[3:]
print data.decode("utf-8")