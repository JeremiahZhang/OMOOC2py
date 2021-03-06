# 日记交互 移动版

开发环境

- Ubuntu 14.04LTS
- Qpython CN 1.2.2
- ST3
- Android手机：KONKA V976 Android版本4.2.1

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

- [x] 探索 本地 push 到 Qpython 移动端
- [x] 如何进行本地调试 最小反馈时间 minimize Check out time
- [] 极简日志交互系统
	- [x] 探索 [QPython 开发 WEB APP](http://wiki.qpython.org/zh/webapp/sample/) 嗯 这是在手机上的 现在是要在 Local 编程开发
	- [x] 移动端
	- [] CLI 命令行
	- [] 和微信接通 

***

## 3 探索

目标

- [x] 如何进行 本地web app 开发
	- 已经明白 将本地代码push到Qpython
	- 然后直接在本地 使用 python 命令
	- ssh与收集联通 
	- 参见 **运行** 部分 如

			# cd /storage/sdcard0/com.hipipal.qpyplus/scripts
			# /data/data/com.hipipal.qpyplus/files/bin/python transhello.py

- [x]如何 push 到 qpython 移动端
	- 发现可以将代码直接转化为[QRcode](http://qpython.com/#qrcode) 二维码 用Qpython 扫描即可 恩 这个方法也不错 但现在这个方法还是没有 本地直接推送简单 恩 转回 Push
- 主要参考
	- [如何自在的折腾Qpython](http://codelab.qpython.org/pythonic/init-my-qpy-env.html) 

### push or 上传

- [x]使用什么? SSH
- [x] 上传到 哪儿
- [x] 这里得使用 BusyBox 手机也可以像shell一样了

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

![ssh使用](http://dn-jeremiahzhang.qbox.me/qpy01.jpg) 

恩 密码什么的有提示 默认为 admin  
恩 被打断了 明天继续

#### 到底怎么使用SSH

既然知道要用SSH 进入home之后 到底如何操作呢？明白路径 上传到哪儿

- SSHDroid 其实根目录为  

		/data/data/berserker.android.apps.sshdroid/home/

	类似Ubuntu中的终端中使用 ~ 回到的目录

- 要放到Qpython可读的文件目录中吧

>  QPython 环境分:  

> - 只读执行文件起点 /data/data/com.hipipal.qpyplus/files/bin/

> - 可写资源起点以及目录意义:

		/storage/sdcard0/com.hipipal.qpyplus/
		    +- cache         
		    +- lib        各Python版本的库安装入口 
		    +- projects   俺的QPy 项目入口
		    +- scripts    俺的QPy 脚本入口
    		    +- snippets 
		    +- .run        恩 运行 相关

那么知道文件目录 那么就使用 [using SCP](http://support.suso.com/supki/SSH_Tutorial_for_Linux) SCP吧

> SCP is basically a program that uses the SSH protocol to send files between hosts over and encrypted connection. You can transfer files from your local computer to a remote host or vice versa or even from a remote host to another remote host. 

尝试 可以使用

	scp ~/OMOOC2py/_src/om2py7w/7wex0/hello0.py root@192.168.2.100:/storage/sdcard0/com.hipipal.qpyplus/transhello.py

将本地文件 ~/OMOOC2py/_src/om2py7w/7wex0/hello0.py 传输到手机Qpython的可写资源起点 并且更名为transhello.py 不过每次都要输入密码 admin 有点麻烦 效果如图 

![scp ssh传输文件](http://dn-jeremiahzhang.qbox.me/qpy02.jpg) 

现在我将其推送到 /storage/sdcard0/com.hipipal.qpyplus/scripts 目录中 使用以下代码就可以了

	scp ~/OMOOC2py/_src/om2py7w/7wex0/hello0.py root@192.168.2.100:/storage/sdcard0/com.hipipal.qpyplus/scripts/transhello.py

本地hello0.py的代码如下

	# -*-  coding: utf-8 -*-
	import androidhelper
	droid = androidhelper.Android()
	droid.makeToast('Hello, Jeremiah :-) !')

传递过去之后 可以直接在Qpython运行脚本了 并且成功

#### busybox

dama 吼道：

> 等等! SSH 上来后,各种不适应,这什么 shell 环境哪,连 less, tail, vi 都没有 好意思说自个儿是 Linux 嘛?!
搜索才知道,这货叫 ash

> 躲在 /system/bin/sh 基本上什么也不会作
    所以,程序猿有 [BusyBox](http://www.busybox.net/FAQ.html#getting_started)
    一安装,批量将大堆习惯的工具,灌到 system/xbin/

OK 手机下载 BusyBox 恩安装好之后 就可以使用 less tail vi 等命令了 可以直接对手机里面文件如同在PC本地机一样操作了 恩

#### 运行

dama吼:

> 好了,进入下一个阶段: 怎么让 QPyhon 如系统命令一样在 ash 环境中调用我们的脚本?

- 使用 [gen_qpy_env.py](https://gist.github.com/ZoomQuiet/8642464)
	- 推送到Qpython scripts 目录中 并使用Qpython 用脚本形式跑起来

> 肿么,让 shell 环境每次都能自动加载上这堆配置?

按照dama而言 直接使用其代码:(恩 是进入ssh 与手机连接后 的 shell 下)

	# mount -o remount,rw /dev/block/mtdblock3 /system
	# ln -s /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profile /etc/profile
	# mount -o remount,ro /dev/block/mtdblock3 /system

手机重启 SSHDroid 远程ssh登入 测试

![shell自动加载](http://dn-jeremiahzhang.qbox.me/qpy03.jpg) 
	
然后 远程人工使用 shell 调用 我scripts 文件下刚刚从本地传输过去的 transhello.py 文件

	# cd /storage/sdcard0/com.hipipal.qpyplus/scripts
	# /data/data/com.hipipal.qpyplus/files/bin/python transhello.py

不论手机在什么界面下 会跳出 **transhello.py** 运行结果

#### 自动

> 好了,进入最后一个阶段: 怎么让所有的上传->配置->运行->日志收集 全部自动化一键完成?


    自动上传?!(怎么通过公匙的部署,来达到无口令远程登录手机?)
    自动运行手机端的脚本?!
    自动收集日志?

- 探索 使用 [pexpect](http://www.noah.org/python/pexpect/)  查看doc 文档 另 [Pexpect V4](https://pexpect.readthedocs.org/en/stable/) 

恩 DAMA 那部分没读懂 

> 先将本地公匙用口令登录的方式推上手机

发现好像有点远 暂时回来 直接fabirc先

#### Fabric

- 本地安装Fabric
- 直接使用Dama的 fabfile.py文件 放到本周开发目录中
	- 简单修改参数 就可以
	- 本地进行代码编写
	- **fab qpy:script=当前调试脚本.py** 一键上传到手机 并自动运行
	- 在手机上真实操作 好自动化

此处 我将自己的文件 放入 qpython projects中的chaos项目中 并命名为 **hello.py**

然后直接 在本周任务目录下 使用

	fab qpy:script=hello.py 

OK 直接推送并run hello.py 代码 因为没有设置上一步的自动 所以还要输入几次密码

- admin
- 本机管理员密钥
- damin

感觉每一次这样 还是有点重复 恩 没办法了 先这样

日志的运行 暂且不查看了

[ci 代码 copy dama](https://github.com/JeremiahZhang/OMOOC2py/commit/a61bd4ecb1dfd8b7418f85f1388d32306ea8ecb8) 

***

## 4 Qpython Web 本周日志开发

以上只是为了checktime少 经历了这么多时间

### 4.1 初探 Qpython Web APP

[Qpython 开发 WEB APP](http://wiki.qpython.org/zh/webapp/sample/#_1) 

- WEB APP 框架
- 使用SL4A 接口获取地理位置信息
- 调用安卓体系内其他 APP 的公开接口的方法

完成代码 main.py 在此目录下使用 

	fab qpy:script=main.py 

发现 warning

	Warning: Permanently added '192.168.2.103' (RSA) to the list of known hosts

恩 想到 dama 那会也遇到类似

	sed -i -e ’36d’ ~/.ssh/known_hosts

修改还是不对原来是 变成了这个 **192.168.2.103** 修改后 成功 绕了一下 :-)

提交Qpython的代码 直接运行后 可行

### 4.2 极简日志交互

目测 需要和 公网版orWeb版 类似 需要

简单 search 找到 [Python Programming with QPython](http://www.pinoyden.com.ph/index.php?topic=289814.0)  里面有较多教程可以学习 恩

#### home 页面

简单一个home页面 出错。。。

[ci 代码](https://github.com/JeremiahZhang/OMOOC2py/commit/8c7e5b750fe91c2a8f95078f1ced6c79c90cb04a)

	web app launch timeout(10)

恩 再议

测试发现 原来主要是

- 路径目录没有设置 ROOT 
- app.route('/', method='GET')(home) method = POST
的 改为 GET 就OK了
- 注意 这里我直接将 数据文件mydiary.db放入了Qpython的项目目录中 
	- 尝试 直接使用在 home 中添加自动新建db文件 发现 会造成不必要的麻烦 暂时不考虑 直接将db文件放入项目目录中
	- 可以尝试 自己建一个脚本 如果要新建数据db文件 就执行 恩

[ci 代码](ht) 

#### write 文字保存 打印日志

思路是这样

- 将html中的内容抓取过来(第4w已经过了)
- 保存入sql数据文件中([sqlite3 文档](https://docs.python.org/2.7/library/sqlite3.html) )

恩 中文有输入影响么 目测有 实际输入真的有 因为在html 加入了utf-8 出现错误提示 恩 直接将中文tag和 content内容加 decode('utf-8') 解码

[ci 代码 GET 和POST 导致耽误时间了](https://github.com/JeremiahZhang/OMOOC2py/commit/2e45a7731397b092337eeed55413dd639e7fb845)    
[ci 代码 打印日志](https://github.com/JeremiahZhang/OMOOC2py/commit/d1d92774ba99dbb5e4d604b48b399d5a0b2ec660) 

效果:  
![交互日志 效果](http://dn-jeremiahzhang.qbox.me/qpy04.png) 


Friday, 27. November 2015 10:14PM  2h 初探+笔记  未达到心流状态 恩 反省过程中被打断 得手机断开 ok
Saturday, 28. November 2015 11:22PM   1.5h 分解任务于 ssh部分浅尝  
Tuesday, 01. December 2015 12:02AM  3h ssh登录 并传输 自动busybox + 自动 + fabric
Tuesday, 01. December 2015 10:46PM  2h 4.1 部分
Wednesday, 02. December 2015 11:37PM  2.5h home 页面部分 but error
Friday, 04. December 2015 04:58PM 4h 4.2 home 和 write debug 这一段陷入一个醉点 以前做过的 现在还出现问题 说明以前的还不够明白呢




