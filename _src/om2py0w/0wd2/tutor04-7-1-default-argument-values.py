# -*- coding: utf-8 -*-
print 'argument values'
def ask_ok(prompt, retries=4, complaint='yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye','yes'):  	# in
			return True					# return 
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1 
		if retries < 0:
			raise IOError('Refuseink user')
		print complaint
ask_ok('你真的想退出么？', 2000)

print "-o-"*10 
"""The defult valeus are  evaluated at the point of function definition in
the defining scope, so that the codes below will print 5"""
i = 5
def f(arg = i):
	print arg
	pass
i = 6
print f()
"""调用的时候 输出还是5 默认是5 第一次i = 5
调用的时候没有输入参数 所以默认还是5"""
print f(10)
print f()
print 'Important Warning: the default value is evaluated only one'
'''以上 此时 默认还是先前的 i=5 
arg =i '''

print "-o-"*10
print "请注意 这里 mutable object such as a list,dictionary, or instances of most classes"
def f(a, L=[]):
	L.append(a)
	return L
print f(1)
print f(2)
print f(3)

print "---"*10
print "then look at this below can you understand what does it do?"
def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L
	# when i change return L to single return
	# I understand what does it mean when return
"""return without an expression argument returns 
None.""" 
print f(1)
print f(2)
print f(3)