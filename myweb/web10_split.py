#-*- coding:utf-8 -*-
# （3）re.split(pattern, string[, maxsplit])
# 按照能够匹配的子串将string分割后返回列表。maxsplit用于
# 指定最大分割次数，不指定将全部分割。我们通过下面的例子
# 感受一下。

import re

# pattern = re.compile(r'\d+')
# print re.split(pattern, 'one1two2three3four4')

### 输出 ###
# ['one', 'two', 'three', 'four', '']

# （4）re.findall(pattern, string[, flags])
# 搜索string，以列表形式返回全部能匹配的子串。我们通过这个
# 例子来感受一下

# pattern = re.compile(r'\d+')
# print re.findall(pattern, 'one1two2three3four4')
### 输出 ###
# ['1', '2', '3', '4']

# （5）re.finditer(pattern, string[, flags])
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）
# 的迭代器。我们通过下面的例子来感受一下

pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
	print m.group(),

### 输出 ###
# 1 2 3 4

