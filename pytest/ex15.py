# -*- coding:utf-8 -*-
from sys import argv

script, filename = argv

txt=open(filename)#打开一个文件，返回一个文件对象

print "Here's your file %r:"%filename
print txt.read()#从txt文件对象中读取数据

print "Type the filename again:"
file_again=raw_input(">")#使用>作为命令提示符，提示用户输入另外一个文件名

txt_again=open(file_again)

print txt_again.read()