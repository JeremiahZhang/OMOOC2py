# -*- coding: utf-8 -*-
a = dict(one=1, two=2, three=3)						# values containing Numeric types
f = dict(one=1, three=3, two=2)
b = {'one': 1, 'two': 2, 'three': 3}				#
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])	# lists
e = dict({'three': 3, 'one': 1, 'two': 2})			# dictionarys
g = dict({1: 'one', 2: 'two', 3: 'three'})

# position change but the same 
# so the keyword is important in dic 
if a == b == c == d == e == f:
	print 'true'
else:
	print 'false'

if f == g:
	print 'true'
else:
	print '0'

print len(a)
print len(d)

# 什么是dict 中的key key到底是什么？
# d[key]
print d['one']
print """then i know key in dict d is 'one', 'two', 'three', 
but one, two, three is not the key """
print "*" * 20
print a['one']
print "a[one] is not ok, cause NameERROR"
a['one'] += 1
print a['one']
print "*" * 20
class Counter(dict):
	def __missing__(self, key):
		return 0
ccc = Counter()
print ccc['red']
ccc['red'] += 1
print ccc['red']


print '*' * 20
for kw in a:
	print kw

print '*' * 20
keys = sorted(a)  # 这里的sort 是按照key的首字母
for kw2 in keys:
	print kw2

print 'x' * 20
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys() # 可以从字面来理解 viewkeys
values = dishes.viewvalues() # viewvalues()
n = 0
for val in values:
	n += val
print(n)
print n

print '*' * 20
# keys and valus are iterated over in the same order
print list(keys)
print list(values)

print '*' * 20
# view objects are dynamic and reflect dict changes 
del dishes['eggs']
del dishes['sausage']
print list(keys)		# the values and keys are del at the same time 
print list(values)		# 从这里可以看出 动态的变化 values 是跟着变化的