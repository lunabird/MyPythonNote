#-*- coding:utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy返回最后一个元素
#print stuff.pop()# 返回最后一个元素
print ' '.join(stuff) # 这将list变成一个字符串打印了粗来，以空格间隔，并且没有引号
print '#'.join(stuff[3:5]) # 将第三个元素和第四个元素打印出来，中间使用#作为分隔符
print "***".join(stuff)#oh!酷
print stuff[-1:5]#返回[]
print stuff[-1:111111155]#返回最后一个元素
print stuff[0:66]#返回整个数组，没有表示越界的错误
print stuff[1:-1]#从第一个到最后一个，不包含最后一个
print stuff[0:0]