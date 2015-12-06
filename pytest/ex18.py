# -*- coding:utf-8 -*-
def print_two(*args):#星号表示有多个参数，所有这些参数被接受并放到一个list里
	arg1, arg2 = args
	print "arg1:%r, arg2:%r" %(arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1:%r, arg2:%r" %(arg1,arg2)

def print_one(arg1):
	print "arg1:%r" %arg1

def print_none():
	print "I got nothin'."

print_two("Panda", "Ice Bear")
print_two_again("Grizzly", "Panda")
print_one("lunabird")
print_none()