# week_2 日志交互GUI #

- 你的系统 win 7
- 你的编码工具 st2

## 背景 ##

你需要基于第一周的 日志交互作业[https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week01_interact.html](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week01_interact.html) 改写成 极简交互式笔记的桌面版本 GUI

## 开发 ##

- 学习 Tkinter [http://effbot.org/tkinterbook/](http://effbot.org/tkinterbook/) 
	- 你现在 python Help文档摸索了一段时间 发现是不够的 
- 构思
	- 你先前没有好好构思 因为你不熟悉Tkinter 所以你在慢慢熟悉Tkinter模块的时候 才慢慢构思的 
		- 你先决定用 Button widget来实现交互
		- 后来你改为使用Menu widget 来进行交互 就像 win中的`记事本`一样 可以：
	- 打印过去日志
		- 你先想使用Listbox widget来打印过去日志
		- 后来你放弃了 放弃的原因是 Listbox虽然可以打印 但是你发现 可以使用 Text widget 就可以实现
	- 写日志
		- 新建
		- 保存
	- 退出

## Dive in 实现 ##

- 基本框架
	- 使用 Menu 来实现交互
		- PastLog 打印过去日志
		- New 新建日志 
		- Save 最后保存
			- 输入名字
			- Time 未自动加入
		- Exit 退出GUI应用
		- Help 文档帮助使用 
- widget
	- menu 
	- scrollbar
	- Text
	- def function
	- command调用 function

----------

## 代码 ##

[https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py2w/2wex0/main.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py2w/2wex0/main.py)

### 难点 ###

- 你在开发过程中纠结的地方
	- 就是没点击一次 Menu的时候 可以将过去的 widget 消除掉

### 解决 ###

- 函数调用 标记
	
	 	self.readme_Tag    = False  
        self.printLogs_Tag = False  
        self.newLog_Tag = False  
- 消除 Widget

		widget.pack_forget()

以上像个结合使用 就可以将 widget 消除 重新载入你想要的 widget 再进行交互

### GUI 界面 ###

![](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/Gui.JPG)

- `PastLogs` 打印过去日志
- `New` 新建日志
- `Save` 保存日志
- `Exit` 退出 GUI 
- `Help` 帮助文档

----------

## 总 ##

- 冷静自在
- 怎样解题 来实现 怎样编程

----------

# (￣▽￣) #
 
10/29/2015 6:08:05 PM   
10/29/2015 6:18:54 PM  mod