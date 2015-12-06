# -*- coding :utf-8 -*-


import re
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.subn(pattern, r'\2 \1', s)

def func(m):
	print "m.group(1):"+ m.group(1)
	print "m.group(2):"+ m.group(2)
	return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern, func, s)

##
# ('say i, world hello!', 2)
# m.group(1):i
# m.group(2):say
# m.group(1):hello
# m.group(2):world
# ('I Say, Hello World!', 2)
# re.subn(pattern, repl, string[, count])
# 返回 (sub(repl, string[, count]), 替换次数)。