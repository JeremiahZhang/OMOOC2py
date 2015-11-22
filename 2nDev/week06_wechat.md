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

恩 在 微信发送消息 h

就可以在SAE中 得到发送消息 **h** 

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
	
	dev_server.py # 本地运行 然后

	curl -d '[XML请求字串 http://localhost:8080/api/echo # XML请求字串 参考 日志中心 debug可以取得
	
【注意】不是 http://localhost:8080/api/echo/ 我在这里出错了 恩

![本地测试](http://dn-jeremiahzhang.qbox.me/6w00test.jpg) 

这样就不用每次都 push到 sae了 本地操作 可以节省时间那 恩

Thursday, 19. November 2015 10:04PM 大概理解任务内容 和简单分解 形成框架 0 初探微信接入 1.5h [github ci](https://github.com/JeremiahZhang/OMOOC2py/commit/65ab07f9eb8e77615c16ebcdcf113f45fe1131f3)    
Friday, 20. November 2015 09:48PM  到验证错误 等待实名审核中 1h     
Saturday, 21. November 2015 10:47PM  1.5h 0.2 SAE与微信对接   
Sunday, 22. November 2015 11:13PM  2h 输入 h 自动回复消息




