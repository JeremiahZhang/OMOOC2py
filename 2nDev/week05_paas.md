# 极简日志 公网版

- python 应用在SAE上创建和部署
- bottle 如何和SAE结合 实现4w功能
- 实现公网访问
- KVDB 来收集 笔记 分类 管理 备份
- CLI 统计 看看

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

在 config.yaml 和 index.wsgi 所在文件目录(之前建立的sae文件目录)下 使用如下命令

	git init
	git remote add sae https://git.sinacloud.com/jeremiahzhang
	git add .
	git commit -m 'beta 1.0 push'  
	git push sae master:2 # 部署到sae版本2

[git 设置 避免每次都要输入密码](https://help.github.com/articles/caching-your-github-password-in-git/) 

另外请注意 账户和密码为 安全邮箱 和安全密码  雷雨直接用sina 微博登录的 但不是微博的帐号和密码 请注意

然后 再 git add git commit 再

	git push sae master:2

建立第二个版本 如图

03

然后打开 http://jeremiahzhang.sinaapp.com/ 是可行的 之前的不可行

04

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

### 3.2 本地环境开发

参考 http://www.sinacloud.com/doc/sae/python/tools.html#id2

同样 3.1 出错情况 中的 index.wsgi代码 在本地环境开发中 使用 是可以的[commit](https://github.com/JeremiahZhang/OMOOC2py/commit/a476ca008ddc01bd38f2982ea4f48f40f2f6b438) 

猜测 就是在SAE 云端的话 tpl 文件使用问题了

### 3.3 极简日志的公网访问

