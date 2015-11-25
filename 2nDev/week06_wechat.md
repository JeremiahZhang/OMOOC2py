# 日志交互 wechat 版本

- SAE应用 和 微信对接
- 后台消息处理

## 0 初探 微信接入

- 创建微信公众号
	- 嗯 自个儿又申请了一个 [微信订阅号](http://kf.qq.com/faq/120911VrYVrA130805byM32u.html)  玩儿 (名为贝雅书屋) 
- [微信接入指南](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html) 
	- [x] 填写服务器配置(此处url 遇到一个梗 刚开始以为随便填写一个http://love.com 这样行之失效)
		- 搜索 [问题](https://www.google.co.jp/search?client=ubuntu&channel=fs&q=%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E7%BD%AE+%E5%BE%AE%E4%BF%A1&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=VsdNVvizJs_D8AfV6qvgBQ#safe=off&channel=fs&q=%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E7%BD%AE+%E5%BE%AE%E4%BF%A1+url+gitbook) 
		- 恩 看来 wechat要可以和 SAE云应用 对接那 上周SAE是为这周准备的 ok
		- 大妈的[chaos2wechat 1.1.131010 documentation](https://chaos2wechat.readthedocs.org/en/latest/ch00/try.html#id15) 需要简单参考
		- 目前需要理清SAE和wechat对接 URL问题 恩 然后 验证服务器地址有效性 到最后实现开发
	- [x] 验证服务器地址有效性
	- [x] 依据接口文档是实现业务逻辑
		- 配置好以上 2个 才能成为 开发者嘛

### 0.1 服务器配置

#### 0.1.1 创建SAE应用

同5w [日志交互公网版](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week05_paas.html) 类似 建立SAE应用 自个儿建立的应用名为: beiyastudy 恩所以网域为: http://beiyastudy.sinaapp.com

SAE 应用文件目录

	/path/2/your/sae/
		+ config.yaml		应用配置
		+ index.wsgi 		应用根代码

code here [代码](https://github.com/JeremiahZhang/OMOOC2py/commit/60b21f27c09f2302d06474ac1c833ddd87c6c9f1) 

使用 git push 到 sae git 库
 
部署效果 访问 http://beiyastudy.sinaapp.com/
可以 日志中心 查看访问日志

![访问日志](http://dn-jeremiahzhang.qbox.me/6w01sae.jpg) 

#### 0.1.2 建立与微信对接

进入微信公众号的开发者中心 进行配置:

![服务器配置](http://dn-jeremiahzhang.qbox.me/6w02wechat.jpg) 

- 出现 token 验证错误
	- 搜索 到 [需要认证](http://www.cnblogs.com/txw1958/p/wechat-tutorial.html) 
	- 好吧 果然 等待认证中


### 0.2 验证服务器有效性 SAE和微信对接

上面 等待 sina认证 恩 速度还蛮快的 一天之内 好的

认证完之后 还是出现 token问题 sina 实时查看问题

![3error](http://dn-jeremiahzhang.qbox.me/6w03online.jpg) 

想应该没问题 那么就是 第一反应 index.wgsi 文件问题

继续 dama的chaos 

更改并新增文件: 结构目录

/path/2/my/saewechat/
  +- config.yaml    应用配置
  +- config.py      全局配置
  +- index.wsgi     应用根
  +- module/        模块
  |     +-  utility.py
  +- static/        静态文件 
  |     +-  js/ 	# 暂时未加 以下 
  |     +-  css/
  |     +-  img/
  +- templates/     模板文件 
  |     +-  base.html  # 暂时未加 以下
  |     +-  404.html
  |     +-  ...
  +- web/           应用代码
        +-  __init__.py
        +-  mana4cli.py # 未加 恩
        `-  mana4api.py 

[代码这里](https://github.com/JeremiahZhang/OMOOC2py/commit/f4cfdab72e5cc9fcd09f5a2b773a1d264f1add0e) 

注意 在这里 遇到了一个坑

![4error](http://dn-jeremiahzhang.qbox.me/6w04error.jpg) 

恩 原来search 到大妈也问了 [dama wen](https://groups.google.com/forum/#!msg/sae-python/7jwgsVcGBxA/XYDSLyLGcNkJ) 

恩 手动将 [bottle] push到sae git库 然后 成功了

![5对接成功](http://dn-jeremiahzhang.qbox.me/6w05finished.jpg) 

***

## 1 用户消息-公众号自动应答

### 1.1 [x] 公众号自动应答

#### xml 数据包

SAE 和微信公众号 对接完成后 恩 用户发送信息 公众号没有结果的 就需要设置了 

恩 [接受普通文本信息](http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html#.E6.96.87.E6.9C.AC.E6.B6.88.E6.81.AF) 
数据包 是 XML 形式的 恩 修改代码 [在此查看1](https://github.com/JeremiahZhang/OMOOC2py/commit/62982159d9114353860014444ee01832155ca2d6) 

代码改好之后 push到 sae git 库 在微信中发送 a 

在日志中心查看 访问日志是这样的  

![01访问日志](http://dn-jeremiahzhang.qbox.me/6w01test.jpg) 

{刚开始没有查看错误日志 怎么也看不到 xml 数据包}只感到如下 然后 查看文档 了解 [验证消息真实性](https://mp.weixin.qq.com/wiki/4/2ccadaef44fe1e4b0322355c2312bfa8.html) 

> 在开发者首次提交验证申请时，微信服务器将发送GET请求到填写的URL上，并且带上四个参数（signature、timestamp、nonce、echostr），开发者通过对签名（即signature）的效验，来判断此条消息的真实性。

原来 这还是验证 需要查看错误日志才有 其实是debug了 

错误日志是这样 

![02debug日志](http://dn-jeremiahzhang.qbox.me/6w02test.jpg) 

#### 解析 xml

更改代码 获取 xml 中的 content内容 [commit 代码在此](https://github.com/JeremiahZhang/OMOOC2py/commit/e2c03aa0051b6124c414bcc910d222bba2a5ede2)

恩 在 微信发送消息 hi

就可以在SAE中 得到发送消息 **hi** 

![hiXML获取](http://dn-jeremiahzhang.qbox.me/6w03test.jpg) 

所以进一步 可以使用 [xml.etree.elementtree 模块](https://docs.python.org/2.7/library/xml.etree.elementtree.html) 来 进行解析

#### 回复消息

解析微信发送过来的XML数据包后 就可以得到发送消息内容 之后根据信息 进行反馈 恩

主要使用 xml.etree.elementtree.findtext() 函数 再根据抓取内容进行 反馈 比如 微信端输入 h 我公众号自动反馈信息 为 **Haliluya! Welcome!是也乎!**

[修改的代码](https://github.com/JeremiahZhang/OMOOC2py/commit/6d776a3e75c7b28e660b528ef22205f8171b3687) 

效果:

![自动回复消息](http://dn-jeremiahzhang.qbox.me/6w04wechat.jpg) 

至此 公众号 可以自动应答 不过后续还待丰富

### 1.2 [x] 尝试本地测试

首先在sae 文件目录下 使用
	
	dev_server.py # 本地运行 就是服务端

	curl -d '[XML请求字串 http://localhost:8080/api/echo/ # 恩 这相当与微信端 XML请求字串 参考 日志中心 debug可以取得 

![本地测试](http://dn-jeremiahzhang.qbox.me/6wd000test.jpg) 

这样就不用每次都 push到 sae了 本地操作 可以节省时间那 恩 但要注意在一个目录下 进行本地测试那 恩 看截图文件目录

***

## 2 Dive in 自动应答 + KVDB

### KVDB

官方的文档[kvdb](http://www.sinacloud.com/doc/sae/python/kvdb.html)  介绍比较简单 如下实例

	import sae.kvdb
	kv = sae.kvdb.KVClient()
	k = 'foo'
	kv.set(k, 2) # k 是key 2 是value 恩 dict字典也可以做value
	kv.delete(k)
	
	kv.add(k, 3)
	kv.get(k)
	
	kv.replace(k, 4)
	kv.get(k)
	
	print kv.get_info()


上面 自动应答完成 那么就进一步探索 继续参考 开头dama的教程 [设计](https://chaos2wechat.readthedocs.org/en/latest/ch02/try.html#id14) 

> -  关注者OpenID对一个公众号是唯一固定

[修改代码1](https://github.com/JeremiahZhang/OMOOC2py/commit/77236587e1b33b841d893298bd105a78efa06856) 

直接本地测试（当前文件所在目录）

	$ dev_server.py –kvdb-file=mykv.db 

【注意】 首先在当前文件目录下建立mykv.db 恩 可以 touch mykv.db 如果不建立 会报错 提示没有该文件

恩 不懂 可以 如下 获取帮助

	$ dev_server.py --help
 
恩 可行 push 一次 但是dama的代码 要让人自己填补的  
自己在本地测试的时候 出现过 address 被占用 就是参考 --help文档来解决的 重新启用新的 host 和 port 就搞定了 恩

	$ dev_server.py --port=8000 --host=localhost --kvdb-file=mykv.db

### 修补代码 理解

这里主要是 

	 if None == usr:
                # 首次应答,没有建立档案
                KV.set(uid, {'em':'address'})
                content = "建立档案\n输入你的邮箱如\nem:foo@bar.com"

在调试的时候 突然发现 恩 value 可以是字典的 然后才有 usr['em'] 修改和取值用呢

[修改的代码](https://github.com/JeremiahZhang/OMOOC2py/commit/bc9d381262ff15f0c16a6928c8f131f36b6f2922)

恩 后来 就再添加几行 恩 向一个姑娘表白了 恩恩 要勇敢 勇敢 勇敢

[修改之表白代码](https://github.com/JeremiahZhang/OMOOC2py/commit/4dbcdca5e7103c5c30cadfe1d10fc58321f49139)

好了 有了以上的基础 就可以实现 笔记的开发 了 只要再修改修改就可以了 恩

### 3 微信公众版 日志交互

- 0 写入帮助文档 h 可以返回帮助文档 
- 1 一行一行输入 然后 在微信端可以使用 **n:这是日志** 输入日志并保存 **hist** 参看日志 但是只是最近一次输入的 [代码迭代](https://github.com/JeremiahZhang/OMOOC2py/commit/8dfc42f983cb8ff8c0e86437b523d9b1d8a3662b) 
- 2 需要将历次的笔记都返回给微信用户 恩 尝试理解
	- 官方文档 查看字典的使用
	- 使用 "".join() 函数 将 list 转化为 str
	- [迭代](https://github.com/JeremiahZhang/OMOOC2py/commit/bc8830e77a1ae3e8d3f46cf847d2703c9543b71f) 
	- 输入的历史记录是无序的 就需要排序了 
- 3 解决 usr 字典 排序问题
	- 恩 直接sort 根据 自己定义的 key 来排序
	- 这里是代码[迭代](https://github.com/JeremiahZhang/OMOOC2py/commit/8f3790cc05486c7054b3edf581585c472797e4e4) 
- 4 简单修补一些 help
	- [代码](https://github.com/JeremiahZhang/OMOOC2py/commit/81d2b2b185acdf22191ba8e98a220d783741a136) 

本地测试好 就push了 后再微信测试发现 

### 日志+时间+排序

- [x] 历史日志 还是无时间排序 恩 准备添加时间排序
	- 恩 查看 微信发送过来的XML数据包 本来就有时间戳 那么 直接将这个时间戳转化为localtime 好了 迭代添加时间戳 但历史日志没有加入该时间 [迭代代码](https://github.com/JeremiahZhang/OMOOC2py/commit/a0512a84f70e33b0ced117308a16dafba9442880) 
	- 在历史日志中加入输入日志的时间 [迭代代码](https://github.com/JeremiahZhang/OMOOC2py/commit/986b0816646f236816f459262bd07413be7cefc8) 
- [x] 添加删除用户日志数据 功能 [迭代代码](https://github.com/JeremiahZhang/OMOOC2py/commit/fde49ec4353a93f70226dd0fa54f187704126130) 
- [x] 还有就是 不会打印所有的日志 这个猜测是KVDB的问题 在前面的学习中也存在 没有解决 会一直留存到现在恩 的解决
	- 后来删除日志数据 好像正常了 后续留待观察 恩

## 4 微信版日志 CLI

程序员 都要用 CLI 来调控 这才符合黑客条件嘛 dive in 得参考下 这个[CLI执行](https://chaonet.gitbooks.io/pythoncamp0/content/Chapter-2/%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E6%B5%8B%E8%AF%95%E5%91%BD%E4%BB%A4%E8%87%AA%E5%8A%A8%E7%BC%96%E8%BE%91&%E6%89%A7%E8%A1%8C.html) 

## time log

Thursday, 19. November 2015 10:04PM 大概理解任务内容 和简单分解 形成框架 0 初探微信接入 1.5h [github ci](https://github.com/JeremiahZhang/OMOOC2py/commit/65ab07f9eb8e77615c16ebcdcf113f45fe1131f3)    
Friday, 20. November 2015 09:48PM  到验证错误 等待实名审核中 1h     
Saturday, 21. November 2015 10:47PM  1.5h 0.2 SAE与微信对接   
Sunday, 22. November 2015 11:13PM  2h 输入 h 自动回复消息 后修改 本地测试部分  
Tuesday, 24. November 2015 12:54AM  2h 第二部分 做事要专心 专心
Wednesday, 25. November 2015 12:14AM 总2.5h 第3部分   
Wednesday, 25. November 2015 10:29PM 2h 第3部分 恩

总 12.5h 恩 时间整理以下 发现 一次只做一件事情 恩 只做一件
