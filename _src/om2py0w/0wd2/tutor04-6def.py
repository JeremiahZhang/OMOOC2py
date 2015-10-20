# -*- coding: utf-8 -*-
def fib(n):
	a, b = 0, 1
	while a < n:
		print a, # , 是为了一行输出
		a, b = b, a+b
		pass
print fib(2000)
f = fib
print f(100)

def fib2(n):	# 输出list 形式结果 斐波那契数列
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result
f100 = fib2(100)
print f100