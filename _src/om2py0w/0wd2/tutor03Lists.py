# -*- coding: utf-8 -*-
squares = [1, 4, 9, 16, 25]
print squares
# tri = [1 8 27] so this is invalid syntax 语法错了 就像英文语法错误一样 he girl 
print squares[0]
print squares[-1]

print "*" * 20
print squares[-3:]

print '-' * 20
print squares[:]

print '>o<'*10
squares = squares + [36, 49, 64, 81, 100]
print squares

print "it...then... 执行意图 + >= 3倍"
cubes = [1, 8, 27, 65, 125] # did you fine the wrong num?
print cubes
print 'change 65 -> 64'
cubes[3] = 4 ** 3
print cubes
print 'o-o' * 10 
print 'append means what like this'
cubes.append(216)
print cubes
cubes.append(6 ** 3) # append() items at the end of the list
print cubes
cubes.append(7 **3)
print cubes 
print '()' * 10 
print 'if python then coding'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print letters
letters[2:5] = ['C', 'D', 'E']
print letters
letters[2:5] = []
print letters
letters[:] = []
print letters
letters =['a', 'b', 'c', 'd']
print len(letters)
inner_letter_list = ['a', 'b', 'c']
inner_num_list = ['1', '2', '3']
mess_letter_num_list_lists = [inner_letter_list, inner_num_list]
print mess_letter_num_list_lists 
print mess_letter_num_list_lists[0]
print mess_letter_num_list_lists[0][1]
print '模仿 实践 创意'
print "have fun in python star trek"