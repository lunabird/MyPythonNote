# -*- coding:utf-8 -*-
__author__ = 'lunabird'

import re

pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo lunabird')
result3 = re.match(pattern, 'helo lunabird')
result4 = re.match(pattern, 'hello luanbird')

if result1:
	print result1.group()
else:
	print '1 match failed.'

if result2:
	print result2.group()
else:
	print '2 match failed.'

if result3:
	print result3.group()
else:
	print '3 match failed.'
if result4:
	print result4.group()
else:
	print '4 match failed.'