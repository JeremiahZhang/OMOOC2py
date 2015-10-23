# Google search

## 触发 ##

你在折腾自动登录网页的时候 实践了 [实践-1 自动打开浏览器 进行google搜索](https://jeremiahzhang.gitbooks.io/omooc2py/content/1tDoing/01Gowechat.html) 对吧

那次 你的例子只能通过 shell 调用脚本

	python go_google.py
然后搜索的关键词 只是github

这次是你对这个的扩展

- 你不止搜索 github 一个关键词 需要多个
	- 中文关键字能行么？

----------

## 想法 ##

- 你可以在调用脚本时将外部数据（关键字）传递给脚本 让其使用
- 中文关键字呢？你可以用“utf-8”编码解决吧

----------

## 尝试 ##
### 1.传递外部数据（关键字） ###
你可以这样
	
	python go_google.py keywords01 keywords02 ...

让go_google.py脚本 使用传递过去的参数 keywords01 keywords02  
这个你就要使用 `sys` module, `sys.argv[]`

	your_keywords = sys.argv[1:]
这样你的关键词 `keywords01` `keywords02` `...`就可以被脚本使用了 注意 `sys.argy[0]` 是你的脚本全名 `go_google.py`

这样你就得把关键词自动键入到google搜索栏中

代码 go_google.py：

	# -*- coding: utf-8 -*-
	import sys  
	from selenium import webdriver # 这里使用了selenium 模块
	from selenium.webdriver.common.keys import Keys

	print """ Example 1:
    ==========
    
    	* open a new Firefox browser
    	* load the google homepage
    	* search for "your_keywords"
    
	"""
	your_keywords = sys.argv[1:]

	browser = webdriver.Firefox()             # open your firefox browser

	browser.get("http://www.google.com")      # go to google webpage
	assert 'Google' in browser.title          # confirm that title has “Google” word in it

	search_elem = browser.find_element_by_name('q')  # name = "q" is in the search field of the google webpage source code 相当于点击进入了 google 搜索栏

	for keywords in your_keywords:
    	search_elem.send_keys(keywords + " ")

	search_elem.send_keys(Keys.RETURN)    # search keyword Keys.RETURN like keyboard enter or Go

	print "Mission Completed!"

以上可以实现 英文关键字 google 搜索了  
shell调用：

	python go_google.py python tutorail

效果：

1.自动打开firefox浏览器  
2.自动进入 www.google.com  
3.自动搜索 关键字 `python` `tutorial`  
如图：

### 2.中文关键字搜索 ###
1.**问题：**直接调用脚本

	python go_google.py 编程 教程
出错 原因 编码问题

	UnicodeDecodeError: 'utf8' codec can't decode byte 0xbd in position 0: invalid start byte
2.方案1：你可以全部使用UTF-8编码 之前在完成第一周任务-小小交互系统的时候 就已经知道了吧 [week_1_日记交互系统](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week01_interact.html) 添加 

	# -*- coding: utf-8 -*-
	import sys
	reload(sys) # 必须 reload
	sys.setdefaultencoding('utf-8') # 默认编码
使用utf8 can't decode

	UnicodeDecodeError: 'utf8' codec can't decode byte 0xb1 in position 0: invalid start byte
3.**分析**：`for keywords in your_keywords:`中的 `keywords`的类型是 str 但是 `0bx1` 这种格式的  
search 调试 修改 

`search_elem.send_keys(keywords + " ")` 这部分 猜测其中 `keywords` 编码出现问题 尝试

	search_elem.send_keys(unicode(keywords) + " ")
	search_elem.send_keys(keywords.decode("utf-8") + " ")
	search_elem.send_keys(keywords.encode(sys.stdout.encoding) + " ")
	search_elem.send_keys(keywords.decode("utf-8") + " ")
	search_elem.send_keys(keywords.decode() + " ")
	search_elem.send_keys(unicode(keywords, "ISO-8859-1").encode("utf-8") + " ")
各种编码试过 都出现 同上的 `UnicodeDecodeError`   
你不要再花笨功夫了 好好去理解编码的问题吧...

有点累了 你要 KEEP CALM AND GO SLEEPING byebye

10/23/2015 9:33:41 PM


	
	

	

	

	

	





