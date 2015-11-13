# 极简日志 公网版

- python 应用在SAE上创建和部署
- bottle 如何和SAE结合 实现4w功能
- 实现公网访问
- KVDB 来收集 笔记 分类 管理 备份
- CLI 统计 看看

## python 应用在SAE上常见于部署

## bottle 和 SAE 结合

## 实现公网访问

[SAE git 代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git) 

在 config.yaml 和 index.wsgi 所在文件目录下 使用如下命令

	git init
	git remote add sae https://git.sinacloud.com/jeremiahzhang
	git add .
	git commit -m 'beta 1.0 push'  
	git push sae master:1 # 部署到sae版本1

[git 设置 避免每次都要输入密码](https://help.github.com/articles/caching-your-github-password-in-git/) 

另外请注意 账户和密码为 安全邮箱 和安全密码  雷雨直接用sina 微博登录的 但不是微博的帐号和密码 请注意

在这里 雷雨出错了 恩 Internet server error 然后没有更详细的信息了

好吧 可能是 index.wsgi 的问题 雷雨重试 [bottle 框架](http://www.sinacloud.com/doc/sae/python/tutorial.html#bottle) 修改 index.wsgi 为

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

然后 再 git add git commit 再

	git push sae master:2

建立第二个版本 如图

03

然后打开 http://jeremiahzhang.sinaapp.com/ 是可行的 之前的不可行

04

雷雨猜测 是肯定是 index.wsgi 的代码问题 恩