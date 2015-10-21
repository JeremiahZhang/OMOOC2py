# -*- coding: utf-8 -*-
from collections import deque

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
print "List objects and the method"
print """> method insert remove sort modify the list 
         and have no return value printed--
         they return the default None.
         
         list.insert
         list.remove
         list.sort
         list.append
         
         
         funny list!
         cool ha!
         """

print "-"*30
print "## Using List as Stacks 堆客栈"
print "three peeple have lived in stack 客栈"
stack = [3, 4, 5]
print stack.append(6)
print "入客栈 订房 先订先住"
print "6 is the first " + str(stack.append(6))
print "7 is the second" + str(stack.append(7))
print stack

print "出客栈 退房了 后订 先退"
print stack.pop()
print stack.pop()
print stack

print "*"*30
print "using lists as queues"
queue = deque(["Eric", "John", "Michael"])
queue.append("Teery")
queue.append("Graham")
print queue.popleft()
print queue
print queue.popleft()
print queue

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Teery')
print queue
print "Dont care the "" or the '' in the list"

print '*'*30
print "Functional Programming Tools"

def f(x): return x%3==0 or x%5==0
def g(x):
    if x%3==0 or x%5==0:
        return g

print filter(f, range(2, 25))
print filter(g, range(2, 25))

print type(range(2,5))







