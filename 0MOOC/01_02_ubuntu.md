# Go Ubuntu

- Ubuntu 安装 双系统
- Ubuntu 配置 python 开发环境

# Ubuntu 安装 #

昨天你折腾了近8个小时的Ubuntu安装 终于将Ubuntu安装在你原系统为win7的笔记本上 并让笔记本成为了双系统 嗯Cool   
这下 你可以折腾 学习unix

## 触发 ##

win上你让cli折腾的毫无体肤 你又每天买mac     
太恼怒了 于是乎 你准备转向Unix系统试试 那么入门最好的就是Ubuntu  

Linus说：

> - Microsoft isn't evil, they just make really crappy operating systems.  
- Software is like sex: it's better when it's free.

## 安装进程 ##

- 准备阶段
	- 你确定使用USB U盘安装Ubuntu系统 所以你检测你的电脑能否是使用USB Boot[http://www.pendrivelinux.com/testing-your-system-for-usb-boot-compatibility/](http://www.pendrivelinux.com/testing-your-system-for-usb-boot-compatibility/)
	- 你进行了检测 你的电脑是`esc`进入电脑的BOOT 设置 你将先前的`CD ROM` boot修改 为USB BOOT 这样你的电脑就能使用USB U盘安装Ubuntu系统
	- 你从官网下载好Ubuntu14.04.3LTS[http://releases.ubuntu.com/14.04.3/](http://releases.ubuntu.com/14.04.3/) 
	- **Universal-USB-Installer** 下载好之后你就参考[https://help.ubuntu.com/community/Installation/FromUSBStickQuick](https://help.ubuntu.com/community/Installation/FromUSBStickQuick) 安装USB installer [http://www.pendrivelinux.com/downloads/Universal-USB-Installer](http://www.pendrivelinux.com/downloads/Universal-USB-Installer) 这样你就可将下载好的Ubuntu ISO 镜像文件 `刻录`到U盘 并将U盘作为UBS driver 驱动安装系统了
	- **分割磁盘** 在win下 你使用计算机（右击计算机）的`管理`中`磁盘管理` 对空闲的F盘进行 `压缩卷` 分隔出40G 并`删除卷`
- 安装
	- [https://help.ubuntu.com/community/WindowsDualBoot](https://help.ubuntu.com/community/WindowsDualBoot)
	- 使用USB启动安装
		- 进入 install ubuntu
		- 你选择了中文安装 嗯 其实你需要英文的呀 后来你在系统里面自己改好
		- 之后 你选择`自动分区`
		- 会显示你之前压缩的`40g`为空闲的状态
			- 因为win只能有3+1个主分区 所以压缩出来的那`40G`成为了`逻辑分区` 你对那`40G`分割形成Ubuntu挂载点的时候 需要选择`逻辑分区` 不要选择`主分区` 这样你进行为Ubuntu分区的时候 剩余的磁盘（40G的那）就不会显示不可用了 你在这里折腾了漫长时间的
		- 进行挂载点分配 (选择逻辑分区)
			- /boot 101M ext4
			- / 20G ext4
			- / home 10G ext4
			- / usr 5G ext4
			- / tmp 3G ext4
			- swap 2G
		- 一路安装就OK了
- 可选择进入系统
	- 你安装好之后 开机直接进入的是WIN7 
	- 接下来你就使用EasyBCD2.3 来修改了 你参考了
		- https://help.ubuntu.com/community/WindowsDualBoot 中启动部分Master Boot Record and Boot Manager
		- http://neosmart.net/EasyBCD/
- 修改之后 重新启动 你然可以进行选择 是进入Ubuntu还是进入Windows

----------

## 总 ##

- 安装 一定要从元知识开始 直接从Ubuntu官网进行选择 阅读
- 还是回到 元知识
- 还是回到 元知识

嗯 就这样 你可以开始Ubuntu的探索了

27 . 十月 2015

***

# Ubuntu Python 环境配置

从win转到Ubuntu 进行Pyhon学习 恩 尝试回顾走过的坑

## Go 

- 你首先参考 [在Ubuntu下配置舒服的Pyhon开发环境](http://xiaocong.github.io/blog/2013/06/18/customize-python-dev-environment-on-ubuntu/) 
	- 安装pip和virtualenv

			# 安装 pip
			sudo apt-get install python-pip
			# 安装 virtualenv
			sudo pip install virtualenv

	- 安装 git 和 gitflow
	- 安装 bash-it
	- 安装 Sublime Text 2
		- 这个你之前折腾过 [ST2与Py环境配置](https://jeremiahzhang.gitbooks.io/omooc2py/content/0MOOC/SubPy.html) 

以上 你折腾了蛮长时间 因为unix系统还不熟悉 所以尝试起来 暂时挺不顺手的 尤其在安装python的时候 后来：

- 大妈在2wd4的公开课中讲到了 pyenv 你就去尝试了 安装

		git clone https://github.com/yyuu/pyenv.git ~/.pyenv
		git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv # 配置插件
	- 然后你在 ～/.bash_profile 文件 添加 以下这些 干吗用的 猜测配置吧 你也不太清楚

			#   for PyEnv
			export PYENV_ROOT="$HOME/.pyenv"
			export PATH="$HOME/.pyenv/bin:$PATH"
			export PATH="$HOME/.pyenv/shims:$PATH"
			eval "$(pyenv init -)"

	- 而后pyenv安装python就更方便了
		
			pyenv install --list # 查看python所有版本
			pyenv virtualenv 2.7.10 # 安装python2.7.10

以上 pyenv 的确好使啊！

环境配置好了 继续[Python Star Trek](https://jeremiahzhang.gitbooks.io/omooc2py/content/) 

## 总

Ubuntu 刚上手 有点不适应 慢慢适应就好了 接下来 不用win啦 开心

星期五, 30. 十月 2015 08:10下午 