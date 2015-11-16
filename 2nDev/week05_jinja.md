# Jinja2 初体验

https://realpython.com/blog/python/primer-on-jinja-templating/

github commit [ci](https://github.com/JeremiahZhang/OMOOC2py/commit/d986fee3da52553fbe8df1452d21fd7d738385d5) 

最后 一次提交的错误提示 

	Traceback (most recent call last):
	  File "/usr/local/lib/python2.7/dist-packages/bottle.py", line 862, in _handle
	    return route.call(**args)
	  File "/usr/local/lib/python2.7/dist-packages/bottle.py", line 1732, in wrapper
	    rv = callback(*a, **ka)
	  File "run.py", line 10, in template_test
	    return jinja2_template('template.html', my_string='Wheeee!', my_list=[0, 1, 2, 3, 4, 5], title="Home")
	  File "/usr/local/lib/python2.7/dist-packages/bottle.py", line 3609, in template
	    return TEMPLATES[tplid].render(kwargs)
	  File "/usr/local/lib/python2.7/dist-packages/bottle.py", line 3322, in render
	    return self.tpl.render(**_defaults)
	  File "/usr/local/lib/python2.7/dist-packages/jinja2/environment.py", line 989, in render
	    return self.environment.handle_exception(exc_info, True)
	  File "/usr/local/lib/python2.7/dist-packages/jinja2/environment.py", line 754, in handle_exception
	    reraise(exc_type, exc_value, tb)
	  File "<unknown>", line 1, in template
	TemplateSyntaxError: expected token 'as', got 'end of statement block'

不知道原因 待查明