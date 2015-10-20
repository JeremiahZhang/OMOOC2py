# -*- coding: utf-8 -*-

def ask_ok(prompt, retries = 4, complaint = 'yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye','yes'):  	# in
			return True					# return 
		if ok in ('n', 'no', 'nop', 'nope'):
			break
		retries = retries - 1 
		if retries < 0:
			raise IOError('Refuseink user')
		print complaint

# ask_ok('你真的想退出么？', 2000)

def ask_over(prompt):
    while True:
        over = raw_input(prompt)
        print over
        if over in ('yes', 'ye', 'y'):
            break
        elif over in ('n', 'no', 'nop', 'nope'):
            

