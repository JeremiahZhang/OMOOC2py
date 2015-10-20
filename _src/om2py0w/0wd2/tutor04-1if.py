# -*- coding: utf-8 -*-
x = int(raw_input('please enter an interger: '))
if x < 0:
	x = 0 
	print "负数则变为0"
elif x == 0:
	print "零"
elif x == 1:
	print 'single'
else:
	print 'more'

print 'I love python! '
print '-' * 20
words = ['cat', 'window', 'defenestrate']
for w in words:
	print w, len(w)
print '-' * 20
print 'for statement'
for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)  # 将字长大于6的放入words list中的第一个
	elif len(w) < 6:
		words.insert(4,w)
print words
print 'the length of the words list now is %s' % len(words) # len()是num 所以 不能用 + 而是 % 来
print 'the length of the words list now is', len(words) # same as above
