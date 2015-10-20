# week_1 日志交互系统

- [Latest code](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py0w/0wex0/main.py)
- [使用说明](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py0w/README.md)

## 背景 ##

第一周的任务：交互-101

- 极简交互式日记系统
	- 一次接受一行日记
	- 保存为本地文件
	- 再次运行系统时 能打印过往所有日记

### 任务分解 ###

在芝麻星系统中 学习卡片已经分解完 

1. 脚本调用
2. 调用参数
3. 输入中文
4. 持续交互
5. 输出为文件
6. 回读文本数据

我一上来 看完交互任务 分析的时间是比较短的 没有冷静的去分析 而是直接看一个个已经拆解好的子任务卡片了 然后等完成任务的时候 发现卡片还可以翻页 后面就是提示 然而。。。我已经完成。。。 **欲速则不达** 保持冷静 保持冷静 不要太着急 慢慢来 这是**自我探索 分析的旅程** 谨记

----------

## 1-脚本调用 ##

- 什么是脚本
	- 脚本：就是你写代码的容器 你在哪里写代码的，那个文件就是脚本，python的脚本是**.py**格式的文件
- 如何调用
	- win 系统 打开[powershell](https://en.wikipedia.org/wiki/Windows_PowerShell) 
	- python脚本所在本件目录 比如我的`mian.py`在E:\usr\pybeginner\_src\om2py0w\0wex0中 then 在 shell 中输入`cd E:\usr\pybeginner\_src\om2py0w\0wex0`
	- 调用脚本： `python main.py`

以上 可成功调用 python脚本

## 2-调用参数 ##

- 什么参数
	- 就是外部数据 
	- 在shell中输入的数据 
	- 可以被main.py脚本调用

之前在看 @小赖同学 [淘宝搜索](https://wp-lai.gitbooks.io/learn-python/content/0MOOC/taobao.html)教程的时候 了解到原来在shell中输入

	python mian.py keywords1 keywords2 ...

就可以使 main.py 脚本调用 外部数据（参数 关键字词）keywords1 和 keywords2

- 调用外部数据 如	
	- `python invoking_test.py i love python`
- 分析：
	- 使用sys模块（System-specific parameters and functions） 之前已经了解 仍查询help文档：
> This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.  
> 可获得编译器中变量和与交互时所需用的函数

### 1.代码 ###
	# -*- coding: utf-8 -*-
	import sys
	keywords = sys.argv[:] 
	print keywords
	print type(keywords)
- 注意 
	- 通过`sys.argv`将shell中的参数keywords**传递**到python脚本中
	- sys.argv[0]代表的是python脚本的名字 `invoking_test.py`
	- sys.argv[1] 为 keywords1

shell 执行 `python invoking_test.py i love python` 果效：

	['invoking_test.py', 'i', 'love', 'python']
	<type 'list'>

----------

## 3-输入中文 ##

### 问题1 ###

invoking_test.py 代码

	# -*- coding: utf-8 -*-
	import sys
	print '我爱python'
	keywords = sys.argv[:]
	print keywords
shell调用

	python invoking_test.py 我 爱 python
结果

	鎴戠埍python
	['invoking_test.py', '\xce\xd2', '\xb0\xae', 'ptyhon']
可见 `我` 和 `爱`两个外部数据 使用被脚本调用之后 print 在shell中不正常显示中文

但是直接Sublime Text 直接运行是可以 `我爱python`是正常显示的

### 分析 ###

- keywords1 和 keywords2 等是中文的怎么办？
	- 这个和编码相关 折腾下来 发现中文坑
		- 最好写代码的时候 首次全部用英文完成
		- 然后测试中文
		- 要不会很混乱
		- shell与st2编码又是不同的。。。。
	- 不是有`# -*- coding: utf-8 -*-`申明了么？怎么还是没有用
		- 申明只对脚本中的有用
		- 而shell调用脚本 输出就需要解码啦 print '我爱python' 出现乱码
			- 鎴戠埍python
	- 查看官方文档 unicode 然后
		- google search到 [http://www.kryptosx.info/archives/391.html](http://www.kryptosx.info/archives/391.html "python中文编码问题")
	

### 尝试
代码

	# -*- coding: utf-8 -*-
	import sys
	reload(sys) # 必须 reload
	sys.setdefaultencoding('utf-8') # 默认编码
	
	print ('我爱python'.encode(sys.stdout.encoding)) # 编码 输出
	keywords = sys.argv[:]
	for words in keywords:
    	print words,
shell 果效

	我爱python
	invoking_test.py 我 爱 ptyhon
ST2中也正常
done

----------

## 4-5 持续交互 + 输出为文件 ##

- 运行等待输入
	- while 循环
- 退出脚本
	- 是否退出 日志写完以 `end` 结尾代表退出
	- 退出时 是否添加时间 `def ask_date()`
- 输出为文件
	- txt
	- 打开文件`open()` 写入`write()`

代码

	yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']
	no_list = ['no', 'n', 'NO', 'N']

	def ask_date(prompt): # 退出时是否添加时间
    	ok = raw_input(prompt)
    	if ok in yes_list:
        	ur_date = raw_input("Please add date: ") 
    	if ok in no_list:
        	ur_date = "\n"
    	return ur_date

	done = False
	textInput = ""

	writer = open(diary_name, "w") # if the textfile exist it'll be erased

	while (done == False): # 持续输入日志
    	nextInput = raw_input("Please input ur words: ")
    	if nextInput == "end": 
        	inputDate = ask_date("Do you want add date, yes or no?") # 询问退出的时候添加日期
        	writer.write('\n' + inputDate)
        	break
    	else:
        	textInput += nextInput
        	print nextInput
        	writer.write(nextInput + "\n") #  write into textfile.txt and start a new line

	writer.close()
	print ("Here is ur diary: " + textInput) # 你的日志内容

### 问题 ###

时间是手动输入的 是否可以询问之后 自动输入呢？

search stackoverflow [http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python](http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "datetime")

使用 time 模块

	from time import gmtime, strftime
	strftime("%Y-%m-%d %H:%M:%S", gmtime())
help文档中 `time.gmtime` 使用UTC(世界标准时间)的时间 
进而改为`localtime()`

### 执行 ###

添加模块 `from time import localtime, strftime`

修改 `ask_date()` 中的代码
	
	if ok in yes_list:
        ur_date = strftime("%Y-%m-%d %H:%M:%S", localtime()) 

果效

![datetim vic](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_image/01_time_test.JPG)

----------

## 6 回读文本数据 ##

- 可以将过往的日志比如txt文件打印出来
- 让脚本可以对电脑中（操作系统）的文件进行-寻找-打开
	- 使用`os`： `Miscellaneous operating system interfaces`
	- 打开当前目录 `current_dir = os.getcwd()` `os.chdir(current_dir)`
	- 找到txt文件：`glob`模块 `glob.glob(*.txt)` 
- 7.2. Reading and Writing Files
	- 打开 `open(filename,mode)` mode常用如下：
		- "r" : 可读
		- "w" : 可写
		- "a" : append 附加在文件后面 
	- 读取 `read()`

代码：

	import os, glob
	current_dir = os.getcwd()
	print type(current_dir)
	os.chdir(current_dir)

	for file in glob.glob("*.txt"):
    	print(file)
    	file_content = open(file, "r")
    	print file_content.read()
pshell 执行，可以成功读取代码所在文件夹中所有的txt文件 并打印 果效：
![open_read_print](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_image/02_open_read_print.JPG)

----------

## 整合 ##

以上6个子任务 整合成一个完整的脚本 [main.py](https://github.com/JeremiahZhang/pybeginner/blob/master/_src/om2py0w/0wex0/main.py)  

win pshell 中调用 `python main.py 我 爱 Python`

果效：
![diarylog](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_image/03_all_done.JPG)

----------

## 使用 ##

- 模块 
	- sys
	- os
	- glob
	- time
- build function
	- open()
	- file.read()
	- 模块中的func
		- sys.setdefaultencoding('utf-8')
		- sys.argv[]
		- string.encode(sys.stdout.encoding)
		- os.getcwd()
		- glob.glob()
		- strftime()

## 反思 ##

第一周任务下来 先将任务完成了 最后在写教程的时候 又对代码进行了测试 因为都写在了一个脚本中 所以再次测试的时候 就重新来过 消耗了无谓的时间 缺少**全局观** **调正**

完成任务时：

- 分析
- 然后 google site:stackoverflow 进行关键字搜索 对应模块 函数
- help document 查询

PS

- **淡定自在** 任务发布的时候 简单看了一下任务 没有进行太多的分析 总在想赶着完成任务似的 这是不可行 也不可持久的 记住是探索
- **水平** 高手和新手的一个区别 任务分解能力
	+ 学会分析问题 拆解问题 解决问题
	+ Keep calm Keep Thinking Smartly
- **关于教程** 发现自己写的比较冗余？如何改进写教程呢？
- **改进**
	- 遇见问题 或 项目 
		- 分析是**什么**
		- **怎么**做 分解问题 拆解项目
		- 循序渐进
		- 实践 模仿 创意
	- 子项
		- 一个个脚本编写
		- 测试
		- 整合
		- 不要一股脑儿就在 一个脚本中 进行


	