# -*- coding: utf-8 -*-
the_world_is_flat = 1
if the_world_is_flat :
	print 'Be careful not to fall off!'

# this is the 1st comment
spam = 1 	# and this is the 2nd comment
			# ... and now a 3rd!
text = "# this is not a comment because it's inside quotes."
text_diff = '# this is not a comment because it\'s inside quotes. Ple notice the diff'
print spam
print text
print text_diff

print '*' * 20
print 'i need to defined a variable before assign a value'

print '*' * 20
print 'c:\user\name' 		# note this
print r'c:\user\name' 		# notice the r before 

print '*' * 20
print """"\
Usage: thingy [options]		# muti-line to comment like this
	-h 						Display this usage message
	-H hostname 			Hostname to connect to
"""

print '*' * 20
print 'Jesus' + 'love' * 3 + 'you' + 'forever'
print 'py' 'thon'

print '*' * 20
print 'concatenate variables and a literal use +'
prefix = 'py'
print prefix + 'thon'

print '*' * 20
word = 'python'
print word
print "1st letter of python: " + word[-6]
print 'the last letter of python: ' + word[-1]
print '1st letter of python: ' + word[0]
print 'the last letter of python: ' + word[5]
print "'1st letter of python:  + word[6] is wrong because out of range"
print "please notice the above!"

print '*' * 20
print word[0:2] 
print "here 2 index is exclued"
print word[2:5]
print 'same as above'

print '*' * 20
print word[:2]
print "same as above. but notice the below"
print word[4:]
print "here 4 is include!"

print '*' * 20
print "word[42] is out of range but this one below is useful"
print word[2:42]
print word[42:] 

print '*' * 20
print "python string cannot changed like this"
print "word[0] = J but like this below"
print 'J' + word[1:] # this is just concatenate
s = 'ilovejesus'
print len(s)
ss = 'i love jesus '
print len(ss)