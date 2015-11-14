# coding=utf-8
f = open('workfile.log', 'w')

f.write('This is a test\n')

value = ('the answer is ', 42)
s = str(value)
print s

f. write(s)
f.close()