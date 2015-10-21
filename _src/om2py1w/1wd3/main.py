# -*- coding: utf-8 -*-
a = [1, 2 ,3 , 4]
x = [-1, 0]
a.append(x)         # x is list so list x inside list a
print a
print a.index(x)
print a.pop()             # removes and returns  the last item in list a
print """  list.pop([i]) can returns the item
            the square bracket denote the parameter
            is opitional
"""

print a
a.remove(4)
print a
print a.count(2)

b = [-1, 0, 3, -3]
print "b:" + str(b)
b.sort()      # sorted item
print "b.sort(): " + str(b)
b.reverse()   # reverse
print "b.reverse(): " + str(b)