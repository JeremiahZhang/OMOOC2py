# -*- coding: utf-8 -*-
# 枚举 enumerate()
import math
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

questions = ['name', 'quest', 'fav color']
answers = ['jesus', 'the holy father', 'red']
for q, a in zip(questions, answers):
    print 'what is your {0}?  Its {1}.'.format(q, a) # 配对输出 nice

for i in reversed(xrange(1,10,2)):
    print i

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

bible = {'lord': 'jesus', 'saint': 'paul'}
for b, v in bible.iteritems():
    print b, v

raw_data =[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print filtered_data

# in # not in check out the values
# is # is not check out the object
# compares 

print (1, 2, 3) < (1, 2, 4)
print [1, 2, 3] < [1, 2, 4]
print "ABC" < "C" < "Pascal" < 'python'
print (1, 2, 3, 4) < (1, 2, 4)
print (1, 2, ('aa', 'ab')) < (1, 2, ("abc", 'a'))