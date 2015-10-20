# -*- coding: utf-8 -*-
print 2 % 2
for n in range(2, 13):
	for x in range(2, n):
		if n % x == 0:
			print n, 'equals', x, '*', n/x
			break 	# break 的是 最近的for statement 此处是 for x... OR while loop而不是 if 
					# 要不 12 = 2*6 还有 12 = 3 * 4 or 12=4*3 
					# so break() breaks out of the smallest enclosing for or while LOOP 
	else:			# here else: clause belongs to the for loop not if 
					# 这是突破我以前认识的 不同之处
					# 没有找到因子
					# for loop else clause
		print n, 'is a prime number 素数'
for num in range(2,10):
	if num % 2 == 0:
		print '找到一个偶数', num
		# continue	# 继续的下一次 for loop
		break			# 若用break 则for loop 结束了
	print '找到一个数', num
	pass	# pass statement doing noting 可以用来comment 就像我现在做的一样

while True:
	pass 	# busy wait for keyboard interrupt (ctrl+c)
class MyEmptyClass:
	pass 	# this is commonly used to creating minimal classes
			# 什么是最小 class 再学习class 的时候用 关注
def initlog(*args):
	pass # remember to implement this! 我不知道这个用法是什么的？
