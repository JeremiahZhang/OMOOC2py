# 极简日志 公网版

- 极简日志实现公网访问(直接输入网址访问)
	- python 应用在SAE上创建和部署
	- bottle 如何和SAE结合 实现4w功能
- KVDB 来收集 笔记 分类 管理 备份
- CLI 统计 看看

## 0 安装SAE

- install sae (Ubuntu环境)

	sudo pip install sae-python-dev

其他 可参考 [SAE 安装](http://www.sinacloud.com/doc/sae/python/tools.html#id3) 

## 1 创建应用

登录SAE，进入 [控制台-云应用SAE](http://sae.sina.com.cn/), 点击 创建新应用 ，创建一个新的应用jeremiahzhang, 开发语言选择Python

## 2 编辑应用代码

- 在本地 建立新文件目录 比如 sae 在sae 文件下 2个文件
- 创建 应用配置文件 config.yaml

	name: jeremiahzhang
	version: 2 # 因为 雷雨之前 创建过 一个版本 version 1 所以这里为 version 2

- 创建 index.wsgi 这里可以使用web 框架 [bottle 框架](http://www.sinacloud.com/doc/sae/python/tutorial.html#bottle)

		# coding:utf-8
		from bottle import *
		import sae
		import sys
		
		app = Bottle()
		
		@app.route('/')
		@app.route('/write', method='GET')
		def hello():
		    return 'hello jeremiah-bottle demo'
		
		application = sae.create_wsgi_app(app)

## 3 实现公网访问

[SAE git 代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git) 

在 SAE 云端 代码管理 部分 可以查看  应用仓库地址 这里使用Git版本控制 

![py5w02saegit](http://7xo9hk.com1.z0.glb.clouddn.com/py5w02saegit.jpg) 

在 config.yaml 和 index.wsgi 所在文件目录(之前建立的sae文件目录)下 使用如下命令

	git init
	git remote add sae https://git.sinacloud.com/jeremiahzhang  # 这里 jeremiahzhang 是 appname 应用名
	git add .
	git commit -m 'beta 1.0 push'  
	git push sae master:2 # 部署到sae版本2

[git 设置 避免每次都要输入密码](https://help.github.com/articles/caching-your-github-password-in-git/) 

另外请注意 账户和密码为 安全邮箱 和安全密码  雷雨直接用sina 微博登录的 但不是微博的帐号和密码 请注意

然后 再 git add git commit 再

	git push sae master:2

建立第二个版本 如图

![版本master:2](http://dn-jeremiahzhang.qbox.me/py5w03saegit02.jpg) 

然后打开 http://jeremiahzhang.sinaapp.com/ 是可行的 之前的不可行

![error](http://dn-jeremiahzhang.qbox.me/py5w04sae.jpg) 

### 3.1 出错情况

雷雨之前 将 index.wsgi 直接使用4w的代码 如

	...
	app = Bottle()
	
	@app.route('/')
	@app.route('/write', method="GET")
	def input_diary():
	
	    if request.GET.get('save','').strip():
	        diary_words = request.GET.get('words','').strip()
	        diary_name = 'Diary.log' # if not exist then creat
	        diary_file = open(diary_name, 'a+')
	        diary_file.write(diary_words + '\n') # write words your
	        diary_file.close()
	        diary_file = open(diary_name, 'r')
	        diary_content = diary_file.read()
	        diary_file.close()
	        return template('write_words.tpl', content=diary_content)
	
	    else:
	        diary_name = 'Diary.log'
	        diary_file = open(diary_name, 'r')
	        diary_content = diary_file.read()
	        diary_file.close()
	        return template('write_words.tpl', content=diary_content) # 将write_words.tpl文件也放在了 sae文件下

	application = sae.create_wsgi_app(app)

在这里 雷雨出错了 恩 Internet server error 然后没有更详细的信息了

好吧 是 index.wsgi 中自己代码的问题 所以雷雨重试了上面的[bottle 框架](http://www.sinacloud.com/doc/sae/python/tutorial.html#bottle)

KO 云端不能读取 那个日志文件呀 同本地不同哒

### 3.2 本地运行

参考 http://www.sinacloud.com/doc/sae/python/tools.html#id2

本地进行调试

在 配置文件目录下(sae 文件目录) 终端中输入

	dev_server.py

浏览器键入 http://localhost:8080

同 3.1 出错情况 中的 index.wsgi代码 在本地环境开发中 使用 是可以的[commit](https://github.com/JeremiahZhang/OMOOC2py/commit/a476ca008ddc01bd38f2982ea4f48f40f2f6b438) 

恩 删除 .tpl 这个后缀 就可以公网访问了   
不过又出现 直接输入文字 enter 就出错了 （本地测试是没有错的）表示伤心

看文档去 猜测是 核心代码 问题 恩 去修改 多坑 水

### 3.3 极简日志的公网访问 使用 KVDB

想想 还是 SAE 云端读不了 log 文件的 恩这时就要使用 [kvdb](http://www.sinacloud.com/doc/sae/python/kvdb.html?ticket=4669740fb7c760d6d569da04fac5cb56947f8010#kvdb) 

恩 早该知道 kvdb 使用呀 怎么现在才想起来呢

然而 在kvdb 也是 来了个坑 

走过大妈的 [大妈7-42](http://chaos2sae.readthedocs.org/en/latest/ch01/try.html#id10) 

没看懂 哎呀 花了笨功夫 恩 花了时间 为什么没有解决 

后来看了 Alan Lai 同学 的 kvdb 部分 恩 才明朗起来 [公网版日记系统](https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html) 

	kv = sae.kvdb.Client() # 这个设置好后 然后 kv.set add 什么的 之后 push 到云端 就直接是个数据库呀

参考 Alan Lai 同学的代码 仿造 [修改代码](https://github.com/JeremiahZhang/OMOOC2py/commit/056718567b581607b20bc99305ebbf786e54b5c4?diff=split)

然后push到sae 就ko 可以访问了

### 3.4 改换使用Jinja2模板

恩 对刚开始的 页面layout 感到不爽 想起上一周 Dama推荐 [jinja2](http://jinja.pocoo.org/docs/dev/) 模板 去学习了

尝试一个案例 https://realpython.com/blog/python/primer-on-jinja-templating/ 虽然是和 flask 使用的 但是 也换用 bottle嘛 

[代码迭代1](https://github.com/JeremiahZhang/OMOOC2py/commit/aaa13e25c5943586a3655eadf53d95f9f9151d53)
[代码迭代7](https://github.com/JeremiahZhang/OMOOC2py/commit/4fee26bcd8ffeff6e0a2860c84920d68b45f16b8) 

好像 没有抓住主要矛盾 去搞这个去了 哭

学习 之后 使用模板 并进行开发

- 刚开始 添加一个 html 模块 https://github.com/JeremiahZhang/OMOOC2py/commit/d8657cb0f20ee6c4342fad5406944344444cf215
- 使用 tag write 子模块 
	- [tag and write 子模块 commit](https://github.com/JeremiahZhang/OMOOC2py/commit/5a4703c0f30c398d056d37d1202700d23ef8667e) 

最后 push 到 sae 的 git 库

公网显示结果（地址: http://jeremiahzhang.sinaapp.com/）

![公网版效果](http://7xo9hk.com1.z0.glb.clouddn.com/5w06taskfinish.jpg) 
	
本地运行显示结果(localhost:8080)
	
![本地运行结果](http://7xo9hk.com1.z0.glb.clouddn.com/5w07taskfinish.jpg) 

## 后续迭代

- [x] 网页 layout （使用jinja2）
- [x] 历史日志 倒序 
	-  根据time 排序 还有点bug 得进行修改 （不同日期的 前面的日期会在前刚开始）
- [] 对笔记进行分类 tag标签 管理
	- [x] 一开始就输入一次标签 然后 所有日志输入都是在标签下
	- [] 但是如何将 上面的标签 和 日志进行关联 
		- 尝试了 tag global 
		- 关联 tag 出现了问题 主要想不出该如何匹配在一起
- [] 问题 
	- []http://jeremiahzhang.sinaapp.com/ 历史日志 不能全部显示 但是 本地测试 是可以的诺
- [] kvdb 日志 数据备份处理
- [] CLI 交互

Friday, 13. November 2015 09:42PM  1st    
Saturday, 14. November 2015 10:37PM 2try kvdb 公网访问    
Monday, 16. November 2015 10:06PM  网页layout
Tuesday, 17. November 2015 05:18PM  3.4-迭代




