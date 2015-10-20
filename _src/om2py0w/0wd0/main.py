# -*- coding: utf-8 -*-
# 注释 
# 第一行注释为了可以中文输出 如 print just like this print down
# print "我爱python编程 我在学好编程的路上"
import os
# fibo.fib(100)  # according to py 2.7.10 doc
# fibo.fib2(1000) # here is no answer in ST2 how to slove 

def main():  	# 主程序 主“函数” 注意下一行的缩进 注意()中没有参数 
				# refer to the name “main” is just a convention not a requirement
	print 'Hello World!'				# 这里是英文 就用 单 ''
	
	print "This is Alice's greeting."	# 这里出现了 Alice's 以免混淆 就用 双 ""
	print 'This Bob\'s greeting.'
	# 这里bob's 在写的时候 加了\' 以区分 就可以用 单'' 可以与上一行对比

	foo(5, 10) 				# 调用函数 foo
	
	print '=' * 10 			# print 字符串 可以用 这样的形式 嗯 
	print '0' * 30
	
	print 'Current working directory is ' + os.getcwd() # os木块调用 注意 这里中间为 + 
														# 用 % 试过出错 --- % 不能将两个参数连起来 如下
														# TypeError: not all arguments converted during string formatting
	counter = 0  
	counter += 1  							# 计数
	
	food = ['apple', 'oranges', 'cats']  	# list 字符串 
	
	for i in food:							# for 循环
		print i 							# 看看 i 嗯 这里就是 和下面一样
		print 'I like to eat ' + i  		# + 与 % 区别
		
	print 'Count to ten: '
	for i in range(10):						# 爱从0开始
		print i
		
def foo(param1, secondParam):
	res = param1 + secondParam
	
	print '%s plus %s is equal to %s' % (param1, secondParam, res)	# %s 代表string 
	
	if res < 50:
		print 'foo'
	
	elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):	# and or 布尔运算
		print 'bar'

	else:
		print 'moo' # know

	return res	# thsi is a one line comment. 不明白return 我去掉这行 也可以运行
				# The return statement returns with a value from a function.
				# return without an expression argument returns None. 
				# Falling off the end of a function also returns None
	'''A multi-
line string, but can also be a multi-line comment.'''	# 多行注释 用'''comment'''

if __name__ == '__main__':		# 这个原来不知道是什么 将其注释掉 发现
	main()						# 没有任何结果产生 说明 是调用主函数 main()
								# 为什么会这样 本来就这样吧  
								# 执行程序 cause a script to run main()
								# 单独使用 无法使用 OK 就是放在脚本结尾的

# 我自己人工能得出结果
# 编写注意 def if for 这种需要最后 : 不要遗漏
# print 多种形式 尤其是 '%s plus %s is equal to %s' % (param1, secondParam, res)