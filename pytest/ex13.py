#-*- coding:utf-8 -*-
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

age=raw_input("How old are you?")
name=raw_input("What's your name?")
print "what's wrong?",#这里加上逗号，光标还在原来的那一行；不加逗号就会重启一行
doing=raw_input()#记得加上括号

print "hehe your age is %s, your name is %s, you are %s"%(
	age,name,doing)