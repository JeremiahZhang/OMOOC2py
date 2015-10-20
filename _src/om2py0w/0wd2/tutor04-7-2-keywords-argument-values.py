# -*- coding: utf-8 -*-
def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
	print "-- This parrot wouldnot", action,
	print "if you put", voltage, "volts through it."
	print "-- Lovely plumage, the", type
	print "-- It's", state, "!"
parrot(1000)										# 根据位置 确定参数
print "+"*20
parrot(voltage=1000)								# 根据 1 个 keyword arg
print "-"*20
parrot(voltage=1000000, action='V00000000M')		# 根据2个keyword arg
print "+"*20
parrot(action='V00000000M', voltage=1000000)		# 根据2个keyword arg 顺序可以改变
print "-"*20
parrot('a million', 'bereft of life', 'jump')		# 3个位置 arg
print '+'*20
parrot('a thousand', state = 'pushing up the daisies') # 1个位置arg 1个keyword arg
print '+'*20
# parrot()
# error parrot(voltage=5.0, 'dead')
parrot(voltage=5, state = 'dead')
print '+'*20
# error parrot(110, voltage=220)

def cheeseshop(kind, *arguments, **keywords):
	print '-- do you have any', kind, "?"
	print "-- I am sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print '-' * 40
	print keywords
	keys = sorted(keywords.keys()) # 将keywords中的字母按首字母排序的 a b c d等顺序
	for kw in keys:
		print kw, ":", keywords[kw]
cheeseshop("limburger", 
	"it's very runny, sir.", "It's really very, Very runny, sir.", 
	shopkeeper = 'Michael Palin', client = 'John Cleese', sketch = 'cheese shop sketch')

# 现在我已经理解了 这里的coding