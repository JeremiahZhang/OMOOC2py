# Packages

雷雨 今天 在探索 Packages 星球 [packages star](https://docs.python.org/2/tutorial/modules.html#packages) 

## 背景

雷雨 作为 Python 初学者 需要 对 Python Tutorial 有一个探索 1遍是必须的

## 什么是 Packages

雷雨对 packages 和 module 常常混淆了 不清楚两者的区别  雷雨想到底什么是 Packages呀 奥 在 packages star 提到了

> Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A.

恩 Package A 是 submodule B 的 上级 or Parent or 老大  哈利路亚 在雷雨看来 

- a collection of modules is a package
- package 包含着 module 
- 或者 module 是 package 子集 
- 或者 多个modules 组成一个 Package

好了 这下 雷雨 明白了 Python 中 module 和 package 之间的关系 再也不会混淆了

## 怎么使用Packages

雷雨想 那到底怎么使用 雷雨看到 以下 一个 sound package 的结构

	sound/                          Top-level package
	      __init__.py               Initialize the sound package
	      formats/                  Subpackage for file format conversions
	              __init__.py
	              wavread.py
	              wavwrite.py
	              aiffread.py
	              aiffwrite.py
	              auread.py
	              auwrite.py
	              ...
	      effects/                  Subpackage for sound effects
	              __init__.py
	              echo.py
	              surround.py
	              reverse.py
	              ...
	      filters/                  Subpackage for filters
	              __init__.py
	              equalizer.py
	              vocoder.py
	              karaoke.py
	              ...

在 sound 这个 老大级 Top-level package下 有3个 subpackages（formats/effects/filters）   
每个 package（包括子package）首先都有 __init__.py 来初始化 这个package    
这些 __init__.py 文件是为了让 python 识别 这个文件目录下 是 packages  

雷雨知道了这些之后 问 那如何使用这些 packages 呢    
雷雨看到 python 提供几种使用方式：

- 1 葫芦串儿a.b.c 引入

	import sound.effects.echo # 1 葫芦串儿 引入

这样引入 使用就需要这样

	sound.effects.echo.echofilter(input, output, delay=0.7, atten=4) # 葫芦串儿 然后再使用 echo 中的 echofilter 函数
	
- 2 吃掉一个package葫芦a.b 引入

	from sound.effects import echo

使用就这样

	echo.echofilter(input, output, delay=0.7, atten=4)

- 3 直接引入 函数 葫芦

	from sound.effects.echo import echofilter

这样 就需要这样使用了

	echofilter(input, output, delay=0.7, atten=4)

雷雨知道了以上几种方法 建议使用以下这种形式

	from package import item

- 4 还有这种 Importing * From a Package

	from sound.effects import *

雷雨知道 这个 就是将sound下effects package下的所有 .py 都引入了 但是这个使用需要 effects package下的__init__ .py 要有行代码 

		      effects/                  Subpackage for sound effects
	              __init__.py 	    # 就是这个文件 要有行代码

这行代码就是

	__all__ = [ "echo", "surround", "reverse"]

## 什么时候使用

恩 当雷雨需要使用 得用 package 的时候啦 就得 引入啦

## 总

好了 雷雨简单探索了 Package Star 恩 以前雷雨使用的时候 还真不知道这么多呢 

雷雨登上 enterprise 离开了 Package Star 

准备探索另外一个 star

星期二, 10. 十一月 2015 08:49下午 2 tomato

***

# Python Package Install

哈利路亚 这个是雷雨 之前在 win系统 上 探索 package install 
那个时候 雷雨 不知道 真不不知道 package 与 module 的不同呢  
来看看雷雨的探索过程 

## 背景 ##

有一个微信公众号 每次写点内容 总要输入密码 浏览器记录了也没有用   
所以想写一个python脚本 直接调用 登录微信公众号网页[https://mp.weixin.qq.com/](https://mp.weixin.qq.com/)

## 探索

- 经过 Google Search [http://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python](http://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python) 要安装 automating Web browsing Package [twill](http://twill.idyll.org/)
	+ 根据 [easy install](http://peak.telecommunity.com/DevCenter/EasyInstall#downloading-and-installing-a-package) 安装 twill 不行啊
	+ 不知其他package行不行 还待验证
- 居然没有直接去 the Python Package Index [PyPI](https://pypi.python.org/pypi)网页去找 **教训**
- 醒悟过来后 找到[twill-1.8.0](https://pypi.python.org/pypi/twill)
- 安装遇到问题 回归 help文档 Installing Python Modules

## 安装 ##

### 方案-0 Pip install ###
	pip install package_name

### 方案-1 ###

在[PyPI](https://pypi.python.org/pypi)下载对应的Package 一般package 有说明怎么安装 安装说明来也可以  
但是也可以下载 package 使用python进行安装

- 从PyPI下载Packege文件 如[twill-1.8.0](https://pypi.python.org/pypi/twill) gar.gz文件到目录C:\temp
- 解压package压缩包 可以在文件目录中 `C:\temp\twill-1.8.0` 有个setup.py脚本
- 使用Python安装 (window Powershell中)

		C:\temp\twill-1.8.0
		python setup.py build
		python setup.py install
可以成功安装

在使用Twill过程发现

	ImportError: No module named lxml
缺少 `lxml` module 安装 Package [lxml](https://pypi.python.org/pypi?%3Aaction=search&term=lxml&submit=search)使用babun安装

	pip install lxml 
执行 `from twill.commands import *`提示缺少requests模块 No module named requests go on

	pip install requests
执行 又提示
	
	cssselect seems not to be installed. See http://packages.python.org/cssselect/
继续

	pip instal cssselect
总算完工
	
### 方案-2 ###

若在PyPI中的package有安装说明 就直接用command line安装

## 总 ##

- 需求外部 python package babun中 直接`pip install`
- 直接从PyPI中寻找Package
	- 若直接有安装说明 就用cmd line命令安装
- 下载压缩文件 解压 
- 安装 window shell中 安装

### 方案-3 在ubuntu系统上了

假如安装 requests package
 
	sudo apt-get install python-requests # 安装
	

10/20/2015 10:06:09 PM
星期四, 12. 十一月 2015 01:45下午  mod and tranfer





  