# Tmux Explore

雷雨开始了 Tmux 之旅

- 系统 Ubuntu14.04 LTS
- 系统终端 Terminal

什么是Tmux？ 终端多用利器

> tmux is a terminal multiplexer! 
What is a terminal multiplexer? It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. And do a lot more. See the manual.

## 背景

雷雨在4周学习python 完成任务时 会使用较多的终端 然切换之 常头疼烦乱 在想要的多个终端之间找来找去 

雷雨后来尝试直接使用 Ubuntu 自带终端的多个窗口 发现 当前还是只能一个窗口

然 大妈 在公开课 演示时 多个窗口 直接在当前显示 只要快捷键就可以直接切换 太方便了 

雷雨在3wd4课之时 不能再视而不见了 完成了 4w的任务之后 雷雨尝试去 探索以下 Tmux

恩 雷雨虽然之前 探索了解了下 但是 最终还是徘徊在 他人二手资料上 好的 雷雨这回 要回到 tmux manunal 来开始此次 Tmux 之旅了

## 安装

雷雨来到了 [tmux 网站](https://tmux.github.io/)  里面有提示下载 雷雨直接去看了 Github上 [tmux](https://github.com/tmux/tmux) 的README 说明 

### 尝试1
雷雨尝试了 Readme中的：

	$ git clone https://github.com/tmux/tmux.git
	$ cd tmux
	$ sh autogen.sh  # 在这里就出错了
	$ ./configure && make

错误提示：

	autogen.sh: 15: autogen.sh: aclocal: not found
	aclocal failed
没有发现aclocal 没去管

### 尝试 2

后来 雷雨直接 使用

	sudo apt-get install tmux

来安装的 发现安装的时 1+的版本

恩 想装[tmux2.0](https://gist.githubusercontent.com/P7h/91e14096374075f5316e/raw/6c7eec878900d0e4e196f556360d1b9ceaf523bb/tmux_install.sh)  使用该方法

	# tmux v2.0 installation steps for Ubuntu 14.04 (Trusty Tahr)
	tmux -V
	sudo apt-get update
	sudo apt-get install -y python-software-properties software-properties-common
	sudo add-apt-repository -y ppa:pi-rho/dev
	sudo apt-get update
	sudo apt-get install -y tmux
	tmux -V
	
	# tmux v1.9 installation steps for Ubuntu 14.04 (Trusty Tahr)
	sudo apt-get update
	sudo apt-get install -y python-software-properties software-properties-common
	sudo add-apt-repository -y ppa:pi-rho/dev
	sudo apt-get update
	sudo apt-get install -y tmux=1.9a-1~ppa1~t
	tmux -V
	
	# On Ubuntu 12.04 (Precise Pangolin), step 5 would be: sudo apt-get install -y tmux=1.9a-1~ppa1~p
	# On Ubuntu 13.10 (Saucy Salamander), step 5 would be: sudo apt-get install -y tmux=1.9a-1~ppa1~s

这下 

	tmux -V #查看版本 为 2.0

后来雷雨 tmux 命令 无法进入 tmux window 解决方案：

	tmux attach
	pgrep tmux # 这里键入之后 会显示一串数字 雷雨的是16469 然后使用下面一行命令 数字需要使用 pgrep tmux 获得的数字
	/proc/16469/exe attach



## 配置

雷雨安装好 tmux 后 直接在Terminal中 使用：

	tmux

进入 tmux window

但是 之前参考他人教程 可以使用 快捷键 CTRL + B 然后 “ 可以水平分割窗口 雷雨尝试了 没有反应呀

参考 [Ubuntu manunals](http://manpages.ubuntu.com/manpages/trusty/en/man1/tmux.1.html) ：

> Specify an alternative configuration file.  By default,tmux loads the system configuration file from /etc/tmux.conf, if present, then looks for a userconfiguration file at ~/.tmux.conf.

雷雨没有找到 该文件 OK 雷雨想 要么自己新建一个 要么参考使用他人配置好的 雷雨选择了后者

参考 [tony/tmux-config](https://github.com/tony/tmux-config) 

下载

	git clone https://github.com/tony/tmux-config.git ~/.tmux

复制文件到雷雨的 Home：

	ln -s ~/.tmux/.tmux.conf ~/.tmux.conf

这样 雷雨tmux 有了 .tmux.conf 配置文件

## 使用

### 进入tmux

终端中 雷雨直接键入

	tmux

进入 tmux window 001

### 查看 keyboard shortcuts

因雷雨 使用了 他人的配置文件 .tmux.conf 所以需要根据该配置文件来

- Control + a before any command
- Ctrl + a then ？ # 查看 绑定的快捷键

查看到了 bind key 002

## 体验

### 分屏

1

雷雨查看了配置的快捷键之后 尝试 分屏

同时 Ctrl + a 然后 “ 分屏 如下 003


现在 雷雨的光标在 下面 分割的一个 window 恩 如何回到上面的 window 呢

2

键盘直接 Ctrl a 之后 鼠标滚轮一滚就到上面的window去了

雷雨 光标在 上面一个window之后 相 竖直分一个 window 键盘直接

Ctrl a 然后 % 

效果 004

雷雨看出 直接 在上面一个 window 中 水平分出了一个 window（原来是在光标所在的屏分出来的）

3

现在分成3个window之后 如何切换呢？ 雷雨发现 这样

键盘 Ctrl a 之后 直接使用 键盘 上下左右 箭头就可以切换了

4

雷雨想回到最初的一个window 恩 

Ctrl a 之后 ! (英文输入法下的哦)

星期二, 10. 十一月 2015 05:40下午 

