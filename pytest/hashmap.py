# -*- coding:utf-8 -*-
def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets. """
	aMap = []#一个列表
	for i in range(0, num_buckets):#这个列表有256个插槽
		aMap.append([])
	return aMap

def hash_key(aMap, key):#将字符串转换为数字，这个数字就是bucket_id
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):#使用hash_key来找到一个key所在的bucket
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
#使用get_bucket来获得一个key所在的“bucket”，它通过查找bucket中的每一个元素来找到对应的key。
#找到对应的key之后，它会返回这样一个元组(i, k, v)，i表示的是key的索引值，k就是key本身，v是key对应的值。
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v

	return -1, key, default


#它使用get_slot来获得 元组(i, k, v) 但是只返回v
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)	
	return v
#设置一个key/value键值对，并将其追加到字典中，保证以后再用到的时候可以获取的到。
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i>=0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#the key does not, append to create it
		bucket.append((key, value))
#删除一个key, 找到key对应的 bucket，并将其从列表中删除。
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
#它能打印出hashmap 中的所有东西，并且能帮助你理解字典的细微之处。
def list(aMap):
	"""Print out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v