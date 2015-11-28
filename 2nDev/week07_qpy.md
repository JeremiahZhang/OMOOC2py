# 日记交互 移动版

## 0 初探

主要是看资料 了解相关资讯 来分解任务 一步步完成

- [Installable Web Apps with the WebApp Manifest in Chrome for Android](https://developers.google.com/web/updates/2014/11/Support-for-installable-web-apps-with-webapp-manifest-in-chrome-38-for-Android) 
- 大妈ZQ的[如何自在的折腾QPy ](http://codelab.qpython.org/pythonic/init-my-qpy-env.html#_1) 
- [qpython wiki](http://wiki.qpython.org/) 
	- [start qpython](http://wiki.qpython.org/doc/how-to-start/#a-dashboard) 
	- [hello world qpython](http://wiki.qpython.org/doc/hello-world/) 
	- [Qpython 开发web app](http://wiki.qpython.org/zh/webapp/sample/) 
	- [QPy 编程向导](http://wiki.qpython.org/zh/doc/program_guide/#_2) 
		- python 核心 2.7.2 可自己更新
		- 三种运行模式
			- console 控制台
			- kivy 图形模式
			- webapp模式

***

## 1 浅尝 Qpyhon

- 得下载 Qpython
	- Google play 是么办法了 可以 腾讯应用宝 我用的刷机精灵
	- 恩 直接进入页面 中文版的 一看就能理解
		- 终端 python shell
		- 编辑器
		- 程序
		- 库
		- 社区 恩讨论
- console 模式
	- 使用 **编辑器** 编写了一个 简单的 hello world 恩
	- myhello.py 然后运行 恩 体验是 就是手机版的 python 恩 但是呢 手机端 输入比较恼火
- web app 模式还没有尝试

以上 探查下来 手机上直接 webwpp开发是不可能了 为了符合最小时间反馈 恩 得考虑使用 本地测试 看了一遍大妈的折腾 下面准备探索
	
- 本地进行 webapp 如何进展
	- 本地PC端编写代码
	- push Qpython
	- but 最小反馈 得使用
		- 本地调试
		- 得探索[fabric](http://www.fabfile.org/) 

***

## 2 分解任务

- [] 探索 [QPython 开发 WEB APP](http://wiki.qpython.org/zh/webapp/sample/) 嗯 这是在手机上的 现在是要在 Local 编程开发
- [] 探索 本地 push 到 Qpython 移动端
- [] 如何进行本地调试 最小反馈时间 minimize Check out time
- [] 极简日志交互系统
	- [] 移动端
	- [] CLI 命令行
	- [] 和微信接通  

***

## 3 Qpython 探索

- 目标
	- 如何进行 本地web app 开发
	- 如何 push 到 qpython 移动端
		- 发现可以将代码直接转化为[QRcode](http://qpython.com/#qrcode) 二维码 用Qpython 扫描即可 恩 这个方法也不错 但现在这个方法还是没有 本地直接推送简单 恩 转回 Push
- 主要参考
	- [如何自在的折腾Qpython](http://codelab.qpython.org/pythonic/init-my-qpy-env.html) 

### push or 上传

- 使用什么
	- SSH
- 上传到 哪儿
	- 这里得使用 BusyBox

#### SSH 

- 参考 [SSHDroid](http://www.upubuntu.com/2012/05/access-your-android-files-and-folders.html) 
去应用市场下载SSHDroid [google play](https://play.google.com/store/apps/details?id=berserker.android.apps.sshdroid&hl=en) 并简单了解

那么怎么和PC链接 恩 上面 Google play 中有这样的介绍

> Linux users:
	- File Transfer: natively supported by most file managers (like Nautilus or Dolphin), just enter the sftp address displayed as "Location".
	- Remote Shell: run 'ssh' from the terminal.

因为我使用Ubuntu 所以关注的是这个 还有 win 和 mac 平台的

恩 所以我要使用 ssh 怎么用呢?

- [1 直接使用 ubuntu 的 file](http://www.upubuntu.com/2012/05/access-your-android-files-and-folders.html) 不行 不适合我的14.04

既然都提示要使用终端使用 ssh 了 那么 就 ssh 参考

- [sshdroid via terminal ](https://www.youtube.com/watch?v=uA9GCw7Nw5w) 

原来这么就这么简单 刚开始看 ssh 提示 没懂

图片001

恩 密码什么的有提示 默认为 admin

Friday, 27. November 2015 10:14PM  初探+笔记 2h 未达到心流状态 恩 反省过程中被打断 得手机断开 ok

