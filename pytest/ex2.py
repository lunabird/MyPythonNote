# -*- coding: utf-8 -*-
#输出时要使用%s，一般调试程序输出的时候可以用%r
formatter = "%s %r %r %r"
print formatter %(1,2,3,4)
print formatter %("你是谁",'two','three','four')
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
	"I had this string.",
	"That you could type up right.",
	"But it didn't sing",
	"So I said goodnight."
)