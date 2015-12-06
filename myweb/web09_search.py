# -*- coding:utf-8 -*-
# （2）re.search(pattern, string[, flags])
# search方法与match方法极其类似，区别在于match()函数只检测re是
# 不是在string的开始位置匹配，search()会扫描整个string查找匹配，
# match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配
# 成功的话，match()就返回None。同样，search方法的返回对象同样
# match()返回对象的方法和属性。我们用一个例子感受一下


import re

pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
search = re.search(pattern, 'hello world!')
match = re.match(pattern, 'hello world!')
if search:
	# 使用Match获得分组信息
	print search.group()

if match:#match（）只有在0位置匹配成功的话才有返回
	print match.group()
else:
	print "match failed!"
### 输出 ###
# world
# match failed!