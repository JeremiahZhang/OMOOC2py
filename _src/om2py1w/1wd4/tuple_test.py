# -*- coding: utf-8 -*-
a = [-1, 1, 66.25, 333, 333, 1234.5]
print a.count(333)

del a[0]
print a

a.pop()
print a

del a[:1]
print a
del a

t = 12345, 54321, 'hello!'
print t

u = t, (1, 2, 3, 4, 5)
print u

a = [t, (1, 2, 3, 4, 5)]
print a  # tuples in list

# tuples are immutables

s = [1, 2, 3] # but lists are mutable like this
s[0] = 4
print s

# but tuples can contain mutable object
list1 = [1, 2, 3]
list2 = [3, 2, 1]

v = (list1, list2)
print v

empty = ()
print len(empty)

singleton = "hello", # tuple
print len(singleton)
print singleton

singleton = "hello" # string
print len(singleton)
print singleton

cool = "i", "love", "python!"
print cool
x = "i"
y = "love"
z = "python!"
x, y, z = cool
print cool  # cool is the same as above