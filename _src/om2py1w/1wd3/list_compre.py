# -8- coding: utf-8 -*-
from math import pi
print '*'*30
print "List comprehensions"
squares = []
for x in range(10):
    squares.append(x**2)

print squares

squares = [x**2 for x in range(10)]
print squares

squares = map(lambda x: x**2, range(10))

a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print a

combs = []
for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))


print combs

print "如果有嵌套的话 list 注意()使用"

vec = [-4, -2, 0, 2, 4]
a = [x*2 for x in vec]
print a
b = [x for x in vec if x >= 0]
print b
c = [abs(x) for x in vec]
print c

freshfruit = ['     banana', '      loganberry', '      passion fruit ' ]
d = [weapon.strip() for weapon in freshfruit]
print d

print """string.strip(s[, characters])
        
        1- Return a copy of the string with leading and trailing characters removed. 
        2- If chars is omitted or None, whitespace characters are removed. 
        3- If given and not None, chars must be a string; 
            the characters in the string will be stripped from the both ends of the string this method is called on.

    """
e = [(x, x**2) for x in range(6)]
# e = [ x, x**2 for x in range(6)] is error
print e

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = [num for elem in vec for num in elem] # 两层嵌套 list in list 相当于matrix
print f

string_pi = [str(round(pi, i)) for i in range(1, 6)]
print string_pi

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

sth = [[row[i] for row in matrix] for i in range(4)] # 从 i 循环先开始
# row[i] in matrix 
print sth

equal_sth = []
for i in range(4):
    equal_sth.append([row[i] for row in matrix]) # 注意这里面的嵌套

print equal_sth

equal_sth_2 = []
for i in range(4):
    equal_row = []
    for row in matrix:
        equal_row.append(row[i])
    equal_sth_2.append(equal_row)

print equal_sth_2

print zip(matrix)  #zip 替代了上面的所有
print zip(*matrix)