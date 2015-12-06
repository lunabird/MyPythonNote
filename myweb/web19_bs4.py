# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,"html.parser")

# print html with pretty format
# print soup.prettify()


# （1）Tag
# Tag 是什么？通俗点讲就是 HTML 中的一个个标签
# 不过有一点是，它查找的是在所有内容中的第一个符合要求的标签
print soup.title
#<title>The Dormouse's story</title>
print soup.head
#<head><title>The Dormouse's story</title></head>
print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# 我们可以验证一下这些对象的类型
print type(soup.a)
#<class 'bs4.element.Tag'>
# 对于 Tag，它有两个重要的属性，是 name 和 attrs
print soup.name
# [document]
print soup.head.name
# head
print soup.p.attrs
# {'class': ['title'], 'name': 'dromouse'}
# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
print soup.p['class']
#['title']
#还可以这样，利用get方法，传入属性的名称，二者是等价的
print soup.p.get('class')
# ['title']
# 我们可以对这些属性和内容等等进行修改，例如
soup.p['class'] = "newClass"
print soup.p
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>
# 还可以对这个属性进行删除，例如
del soup.p['class']
print soup.p
#<p name="dromouse"><b>The Dormouse's story</b></p>





# （2）NavigableString
# 既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文
# 字怎么办呢？很简单，用 .string 即可
print soup.p.string
#The Dormouse's story
print type(soup.p.string)
#<class 'bs4.element.NavigableString'>





# （3）BeautifulSoup
# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,
# 可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获
# 取它的类型，名称，以及属性来感受一下
print type(soup.name)
#<type 'unicode'>
print soup.name
# [document]
print soup.attrs
#{} 空字典





# （4）Comment
# Comment 对象是一个特殊类型的 NavigableString 对象，其实
# 输出的内容仍然不包括注释符号，但是如果不好好处理它，可能
# 会对我们的文本处理造成意想不到的麻烦。
print soup.a
print soup.a.string
print type(soup.a.string)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie 
# <class 'bs4.element.Comment'>
# 所以，我们在使用前最好做一下判断，判断代码如下
if type(soup.a.string)==bs4.element.Comment:
	print soup.a.string