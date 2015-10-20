# -*- coding: utf-8 -*-

x = range(10)
print x
y = range(5, 10)
print 'please notice the range,', y
z = range(1, 10, 3)
print z
a = range(-10, -100, -30)
print a

aa = ['Mary', 'had', 'a', 'litter', 'lamb']
for i in range(len(aa)):
	print i, aa[i]
print '# 使用 enumerate 枚举 same as above let see'
for i, v in enumerate(['Mary', 'had', 'a', 'litter', 'lamb']):
	print i, v
print 'Lets see another thats fun'
for i, v in enumerate(['I', 'LOVE', 'PYTHON']):
	print i, v