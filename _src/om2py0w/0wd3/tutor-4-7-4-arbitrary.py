# -*- coding: utf-8 -*-
def write_multiple_item(file, separator, *args): # arbitrary argument Lists
	file.write(separator.join(args))
print '*' * 20
print range(3,6)
print "this below is a list do you know?"
args = [3, 6] 
print args
print range(*args)
print "can you see the meaning of this code above? yes"

print '*' * 20
def parrot(voltage, state='a stiff', action='voom'):
	print "this parrot would not", action,
	print 'if you put', voltage, 'volts through it.',
	print 'E\'s', state, '!'
d = {"voltage": "FOUR million", "state": "bleedin' demised", "action": "V00M"}
parrot(d)
parrot(**d)

print """ ** operator can deliver keyword 
arguments in dictionaries"""

print '*' * 20
print "lets know the lambda expressions"
def  make_incrementor(n):
	return lambda x: x + n
f = make_incrementor(42)
print f(0)
print f(1)
print f(42)

def make_sum(n):
	return lambda a, b: a + b + n
ff = make_sum(42)
print ff(0, 0)
print ff(1, 1)

print '*' * 20
pairs = [(2, 'two'), (1, 'one'), (3, 'three'), (4, 'four')]
print pairs
pairs.sort(key=lambda pair: pair[0]) 	# I think pair[0] mean the 1st value in lists 
print pairs								# 此处就是按 list中的 （）中 第一位 value 排序 按数字
pairs.sort(key=lambda pair: pair[1]) 	# 此处 （）中 字母排序 abcde的顺序
print pairs
print "print pair[1] display error: name 'pair' is not defined"