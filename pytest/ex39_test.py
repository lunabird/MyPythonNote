# -*- coding: utf-8 -*-
import hashmap

#创建一个州对应的缩写语的映射
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#创建州的基本集合，还有州内的一些城市
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

#添加更多的城市
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#输出一些城市
print '-' * 10
print "NY state has: %s"% hashmap.get(cities, 'NY')
print "OR state has: %s"% hashmap.get(cities, 'OR')

#输出一些州
print '-' * 10
print "Michigan's abbreviation is: %s" %hashmap.get(states,'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states,'Florida')

#输出所有的州的缩写
print '-' * 10
hashmap.list(states)

#输出州的每个城市
print '-' *10
hashmap.list(cities)

print '-'*10
state = hashmap.get(states,'Texas')

if not state:
	print "Sorry, no Texas."

city=hashmap.get(cities, 'TX', 'Does not exist.')
print "The city for the state 'TX' is:%s" %city