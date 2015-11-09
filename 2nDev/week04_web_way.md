# 日志交互 web版

## 开发环境
	- Ubuntu14.04 LTS + 其自带终端
	- SublimeText2 （ST2）
	- Python 2.7.10
	- Firefox 41.0.2 for Ubuntu

## Goal

- 完成极简交互式笔记的WEB版
	- 通过网页访问系统
		-  每次运行时合理的打印出过往的所有笔记
		- 一次接收输入一行笔记
		- 在服务端保存为文件
	- 兼容Net版的，CLI可以进行交互

## 准备

- networks 和 internet 和  port
	- **net** 本地（共用一个cable）多台计算机 可以组成一个局域网络（打CS就可以使用局域网）（Local Area Network） 这些计算机之间的访问 需要通过MAC地址了
	- **Internet** web 就是多个局域网 Network 组成的大的互联网 （打CS时 你需要连上互联网 才能与其他 network 中的 计算机用户 对战） 互联网中不同network中计算机的通信 恩 需要  Internet Protocol (IP) address 再通过 router 和 MAC 地址 进行通讯了
	- **port**  端口 物理端口的话如插usb的那个口 这里的port是 两个机子之间通信过程 通过port来定义
	- [具体参考](http://www.mws.cz/files/PyNet.pdf) 
- 使用web frame work [Bottle 0.12](http://bottlepy.org/docs/dev/index.html)  来看看 Bottle的介绍 bottle是小而全的一个框架 精简而实用 恩 Pythonic 
> Bottle is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library
- 安装Bottle
	- 你可以直接下载[bottle.py](http://bottlepy.org/docs/dev/index.html) 到自己的项目文件夹中
	- 或者 你也可以 安装
		- sudo pip install bottle
- 为什么要用框架
	- web的开发 像建造楼房 打好外部的框架结构 再在此基础上 建造 就容易多了
	- 有 web framework 恩 web的建造 也是容易的

## 熟悉

- 你可以走一遍 [Tutorial: Todo-List Application](http://bottlepy.org/docs/dev/tutorial_app.html#complete-example-listing) 
	- 恩 建议先将代码自己码好 然后 运行理解 
	- 恩** 以亲自码码为容 以复制粘帖为耻 **
- 建立一个简单的网页访问 **webserver.py** 代码如下

		from bottle import *

		@route('/')  # here you can type http://localhost:8010 to see hello welcome
		@route('/hello')
		def hello():
    		return """ # 返回的是html语法 恩 这样网页前端访问 有个基本的样子么
    			<body>
        			<h1>Dear Friend!</h1>
        			<p>This is Your Diary Web! have fun!</p>

        			<ul>
            				<li>Read</li>
            				<li>Write</li>
        			</ul>
    			</body>
			"""
		run(host='localhost', port=8010, debug=True, reloader=1)
- ST2中运行 恩 怎么运行 参考这篇[SubPy](https://jeremiahzhang.gitbooks.io/omooc2py/content/0MOOC/SubPy.html) 
- 打开Firefox（你也可以用其他浏览器）键入 http://localhost:8010/ 就可以直接访你所建立的网页了
- 效果：
![01webhello](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/01webhello.jpg) 

### 理解

- from bottle import * 导入模块 这样你才可以使用 bottle 的命令嘛
- route() 恩 这个 decorator 是为你的网页开路的 上网总得有个路径吧 恩 route() 来为你开路
> The route() decorator binds a piece of code to an URL path.
	- 你可以直接使用 @route('/hello')  这样的话你就需要键入 http://localhost:8010/hello 来访问网页 
	- 在前面 添加 @route('/') 那么直接键入 http://localhost:8010/ 就可以访问上面网页了
	- 可以这么理解 恩 @route('/') 为 @route('/hello') 开好路了 直接 http://localhost:8010/  就可以到达 http://localhost:8010/hello 内容
- **函数** 恩 你有没有看到 @route() 后面都紧跟(或绑定bind)着一个定义的函数？ 这里定义了 def hello() 这样 @route() 开好路 hello() 函数调用了 
	- *hello()* 函数直接返回的是 html 的内容 恩 这样 网页 
	- 什么是 *html*？恩 看这里 [html](https://en.wikipedia.org/wiki/HTML) 简单来说 就是建立网页的 
	- 恩 因为 *hello()* 函数返回的是 html 代码内容 所以打开 http://localhost:8010/ 链接 就直接建立了一个web网页
- **return** 要返回 html代码 这样就可以建立网页嘛
- run() 跑起来 才能 进行网页访问呢
	- host 与 port 主机信息 port 端口信息 
	- **debug = True** 在开发的时候 你可以使用 如果运行出错 会显示错误内容 方便你debug 也可以直接写一行 debug(True) 开发完之后 记得取消哦
	- **reloader = 1** 确认重新加载 恩 这样 你只要修改代码内容保存后 会直接自动加载

***

## Dive In

在 **webserver.py** 中添加代码

	import sqlite3 
	...
	@route('/new', method='GET')
	def new_item():
	
	    if request.GET.get('save','').strip():
	
	        new = request.GET.get('task', '').strip()
	        conn = sqlite3.connect('todo.db')
	        c = conn.cursor()
	
	        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
	        new_id = c.lastrowid
	
	        conn.commit()
	        c.close()
	
	        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
	    else:
	        return template('new_task.tpl')
	...

例外新建 template 模块 new_task.tpl 代码如下：（需保存在与webserver.py同一个项目目录中）

	%#template for the form for a new task
	<p>Add a new task to the ToDo list:</p>
	<form action="/new" method="GET">
	<input type="text" size="100" maxlength="100" name="task">
	<input type="submit" name="save" value="save">
	</form>

### 理解

- sqlite3 [DB-API 2.0 interface for SQLite databases](https://docs.python.org/2/library/sqlite3.html) DB-API 接口
- new_item() 函数
	- 数据库中的交互
	- return template('new_task.tpl')
		- 返回 template 使用的是 new_task.tpl 模块
		- new_task.tpl 模块 代码是 html 格式的 说明 返回的是html网页
		- 在执行过程 中 你会发现 首先执行的是 else 中的 return template
![02webnewitemjpg](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/02webnewitemjpg.jpg) 
		- 然后网页刷新 会执行 if 返回 return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id 这个网页
![03webnewitemback2](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/03webnewitemback2.jpg) 
- 这里用到了 method=‘GET’
	- if request.GET.get('save','')  如果 retrun template网页中 点击了 save 恩 这个if条件就成立 然后就执行 写入数据 并执行 if条件下的 那个return 返回网页 
	- 这说明 request.GET.get() 可以获取网页中的内容 主要是 <form>下的
		- 这里 request.GET.get('save','').strip() 获取 <input type="submit" name="save" value="save"> 的 value 值
		- new = request.GET.get('task', '').strip() 得到的就是 输入框text中的内容
- 其他关于数据库的内容 暂时不管

这样 你就可以使用上面的代码 来进行 **极简交互式笔记的WEB版** 开发了

***

## 极简交互式笔记的WEB版

- 代码 webserver.py

		# coding=utf-8
		from bottle import *
		import sys
		@route('/write', method="GET")
		def input_diary():
		
		    if request.GET.get('save','').strip(): # 之后执行这里
		        diary_words = request.GET.get('words','').strip()
		        diary_name = 'Diary.log' # if not exist then creat
		        diary_file = open(diary_name, 'a+')
		        diary_file.write(diary_words + '\n')
		        diary_file.close()
		        return template('write_words.tpl', content=diary_words) # 再次返回网页
		
		    else: # 刚开始先执行这里的
		        diary_name = 'Diary.log'
		        diary_file = open(diary_name, 'r')
		        diary_content = diary_file.read()
		        diary_file.close()
		        return template('write_words.tpl', content=diary_content)
		
		if __name__ == '__main__':
		    run(host='localhost', port=8010, debug=True, reloader=1) # switched debug off for publich applocations

- write_words.tpl 代码 ：这个

		<p>Write new words into your diary.log:</p>
		<form action="/write" method="GET">
		<input type="text" size="100" maxlength="100" name="words" autofocus>
		<input type="submit" name="save" value="save">
		</form>
		
		<p> Here is your diary content! Darling!</p>
		<textarea rows="30" cols="100">{{ content }}</textarea>

- firefox中键入：http://localhost:8010/write 就可以访问 web 了

效果：
![04webserverresult](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/04webserverresult.jpg) 

- 刚开始打印历史笔记
- 然后输入笔记内容 打印上一次输入笔记内容 非全部历史内容 


### 走的弯路

刚开始的时候 想着 在write中 input_diary() 来一个while循环 使得可以持续输入恩 如

def input_diary():

	done =True
	while done == True：
	
	    if request.GET.get('save','').strip():
	        diary_words = request.GET.get('words','').strip()
	        
		if diary_words == 'q':
			sys.exit()
		else:
			diary_name = 'Diary.log' # if not exist then creat
	        	diary_file = open(diary_name, 'a+')
	        	diary_file.write(diary_words + '\n') # write words your input
	        	diary_file.close()
	
	    else:
	        return template('write_words.tpl')

结果就是 悲惨地发现 在text输入框中 输入一次 Diary.log 日志文件 一直在写入 立马关闭停止 然后Diary.log 文件很大 CLI 命令行 rm 都无法消除 然后 直接把整个文件夹删了 才没有该文件了

你会发现 自然而然地想到 循环来输入 然后 在这里 行不通 走不通之后 你一直刷行 write 网页 然后发现 只要在 if 条件下 再添加 return template不就行了 么

恩 只是上面的 只能在textarea中显示 你上一次的输入 没法显示 所有的历史记录

尝试解决：

- 在if下添加 diary_content 内容 然后 使用template输出 
	
		diary_content=""

		if request.GET.get('save','').strip(): 
			diary_words = request.GET.get('words','').strip()
			diary_name = 'Diary.log' # if not exist then creat
			diary_file = open(diary_name, 'a+')
			diary_file.write(diary_words + '\n')
			diary_content += diary_words
			diary_file.close()
			return template('write_words.tpl', content=diary_content) # 再次返回网页
	- 结果是 还是只能打印上一次的输入笔记
	- 分析 恩 看来 diary_content 还只是局部变量 重新刷了网页之后 还是空了


***

## 总

- web版笔记交互 开发只需要那么几步
	- route 开路
	- Request data
	- 模板 template 使用 html 来建立网页
- 不要纠结小细节 恩 Go

***

## CLI 交互

go check [curl doc](http://curl.haxx.se/) 

## 继续迭代

- [] CLI可以交互
- [] 美化网页 使用 [bootstrap](http://getbootstrap.com/) 
- [] 数据库使用

星期一, 09. 十一月 2015 01:07































		