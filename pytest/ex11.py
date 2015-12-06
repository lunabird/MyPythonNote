# -*- coding:utf-8 -*-
print "How old are you?",#给结尾加上逗号，输入时就会在原来的行而不会重启一行
age=raw_input()
print "How tall are you?",
height=raw_input()
print "How much do you weight?",
weight=raw_input()

print "So, you're %r old, %r tall and %r heavy."%(
	age,height,weight)