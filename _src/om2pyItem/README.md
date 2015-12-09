# 爱搭配 APP

- 项目
	- 中文名: 爱搭配
	- 英文名: Imatch
- 实现功能（最小功能）
	- 默认页面: 3个图片框（衣服-裤子-鞋子）
		- 添加图片
		- 显示图片
	- 含保存
		- 保存时自动截图
		- 开始新一轮搭配
- me: 主要负责开发 Android 移动app版

## 技术难点

已知

- APP 网页框架
	- 图片添加框效果
	- 读取手机图片
- 数据库(到底要不要用数据库呢 不是很清晰)
	- 添加在图片框中的图片是放在数据库呢？
	- 还是直接保存在 相关文件目录中？
- 关于图片:
	- 图片大小 比例 要不要限制 
- 保存功能
	- 保存自动截图
- 编译成APK

## 任务分解

- [x]Qpython 基本框架
- [] APP web 设置  
    	- [x] 上载图片 use bottle
	- [] 页面的html
	- [] 添加图片
	- [] 实现图片添加功能
	- []保存功能 截图
- [] 数据库
- [] 编译成APK

## 迭代进行

- 8wd0 目标初步分解 Qpython webapp 开发框架确定
- 8wd2 
	- 图片上载
		- 参考 [google keywords  search](https://www.google.com.sg/search?client=ubuntu&channel=fs&q=python+bottle+image+upload&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=ZItmVprZD-yW8QeR84TwBg) 
		- [bottle simple example](https://gist.github.com/Arthraim/994641)
		- succeed **host and port should be noted**
	- [html forms](http://www.w3schools.com/html/html_forms.asp)
		- [div](http://www.w3schools.com/html/html_classes.asp)
- 8wd3
	- [x] 构思如何行
		- 使用button来link多个template
	- [x][android app layout](http://www.idangero.us/framework7/docs/app-layout.html#basic-android-material-app-layout)
	- [][Web Fundamentals](https://developers.google.com/web/fundamentals/?hl=en) this need to dive in
		- [x]forms

## 8-10w

- 作品测试
- 集成调试
