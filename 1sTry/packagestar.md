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

	




  