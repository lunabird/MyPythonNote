# -*- coding:utf-8 -*-
__author__ = 'lunabird'

import re
#匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:",m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1,2)
print "m.groups():", m.groups()
print "m.groupdict()", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g  \g'):", m.expand(r'\2 \1  \3')

### output ###
# 1.string: 匹配时使用的文本。
# m.string: hello world!  
# 2.re: 匹配时使用的Pattern对象。
# m.re: <_sre.SRE_Pattern object at 0x00000000026DBCF0>
# 3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
# m.pos: 0
# 4.endpos: 文本中正则表达式结束搜索的索引。
# m.endpos: 12
# 5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
# m.lastindex: 3
# 6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
# 方法：
# m.lastgroup: None



# 1.group([group1, …]):
# 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
# m.group(): hello world!
# m.group(1,2): ('hello', 'world')
# 2.groups([default]):
# 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
# m.groups(): ('hello', 'world', '!')
# 3.groupdict([default]):
# 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
# m.groupdict() {}
# 4.start([group]):
# 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
# m.start(2): 6
# 5.end([group]):
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
# m.end(2): 11
# 6.span([group]):
# 返回(start(group), end(group))。
# m.span(2): (6, 11)
# 7.expand(template):
# 将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
# m.expand(r'\g \g\g'): world hello!