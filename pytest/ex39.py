#-*- coding:utf-8-*-
#创建州和对应的缩写
states={
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}
#创建州对应的城市
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#增加一些新的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#输出一些城市
print '-'*10
print "NY state has: ",cities['NY']
print "OR state has: ",cities['OR']

#输出一些州
print '-'*10
print "Michigan's abbrevivation is: ",states['Michigan']
print "Florida's abbrevivation is: ", states['Florida']

#啊，这只是dict一些嵌套使用的情形
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#打印出所有的州的缩写
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviviated %s" % (state,abbrev)

#打印出州里面的所有城市
print '-' * 10
for abbrev, city in cities.items():
	print "%s has th city %s" %(abbrev, city)

#把上面两个字典的打印放到一起来执行
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviviated %s and has city %s"%(
		state, abbrev, cities[abbrev])

#获取字典中没有的键值对，也不会报错的哦
print '-' * 10
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

#使用默认的值来获取city
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city
