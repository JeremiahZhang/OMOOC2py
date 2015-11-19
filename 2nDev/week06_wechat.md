# 日志交互 wechat 版本

## 0 初探 微信接入

- 创建微信公众号
	- 嗯 自个儿又申请了一个 [微信订阅号](http://kf.qq.com/faq/120911VrYVrA130805byM32u.html)  玩儿 (名为贝雅书屋) 
- [微信接入指南](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html) 
	- [] 填写服务器配置(此处url 遇到一个梗 刚开始以为随便填写一个http://love.com 这样行之失效)
		- 搜索 [问题](https://www.google.co.jp/search?client=ubuntu&channel=fs&q=%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E7%BD%AE+%E5%BE%AE%E4%BF%A1&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=VsdNVvizJs_D8AfV6qvgBQ#safe=off&channel=fs&q=%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E7%BD%AE+%E5%BE%AE%E4%BF%A1+url+gitbook) 
		- 恩 看来 wechat要可以和 SAE云应用 对接那 上周SAE是为这周准备的 ok
		- 大妈的[chaos2wechat 1.1.131010 documentation](https://chaos2wechat.readthedocs.org/en/latest/ch00/try.html#id15) 需要简单参考
		- 目前需要理清SAE和wechat对接 URL问题 恩 然后 验证服务器地址有效性 到最后实现开发
	- [] 验证服务器地址有效性
	- [x] 依据接口文档是实现业务逻辑
		- 配置好以上 2个 才能成为 开发者嘛

### 0.1 服务器配置

#### 0.1.1 创建SAE应用

同5w [日志交互公网版](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week05_paas.html) 类似 建立SAE应用 自个儿建立的应用名为: beiyastudy 恩所以网域为: http://beiyastudy.sinaapp.com

#### 0.1.2 建立与微信对接

### 0.2 验证服务器有效性

Thursday, 19. November 2015 10:04PM 大概理解任务内容 和简单分解 形成框架 0 初探微信接入