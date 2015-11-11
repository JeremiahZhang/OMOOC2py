# Input and Output Star

1
雷雨 今天 乘坐 Enterprise 来到 Input and Output Star 咦 这是一个怎样的星球呢？

输入于输出么 就是

- 你输入 python 接受
- 你要求输出 python 就输出

包括：

- 输出格式化
- 读写文件
	- 文件对象方法
	- json

## 输出格式化 之旅
#### 1 雷雨在这里了解到 目前遇到过三种方法 来写 values

- expression statements
- ==print== statement
-  ==write()== 函数

#### 2  雷雨 在这个星球上 了解到 两种方式来 format 自己的 output

- the first way is to do all the string handling yourself 雷雨不明白这个到底是什么意思 让 string 自己处理自己 原来 是这样
	- using string slicing and concatenation operations you can create any layout you can imagine 使用 string 切片 然后再 连起来 恩 就像 雷雨以前吃的葫芦串 串起来
- use ==str.format()== 方法 两种 将 values 值 转化为 strings的方法
	- ==repr()== 函数 这个将 alues 转化为 编译器去读的 
	- ==str()== 函数 这个 将 values 转化为 雷雨 容易读 和理解的

哦 什么是 values 阿 恩 比如 strings numbers / structures（lists dictionaries）

雷雨看到的例子：
	
	>>> s = 'hello, world.' # string
	>>> str(s)
	'hello, world.'  # 看到两者的区别了么 雷雨能读的
	>>> repr(s)
	"'hello, world.'" # 这里输出的 请注意了 编译器能读的

	>>> str(5) # number
	'5'
	>>> repr(5) # 这两个是一样的
	'5'

	>>> hello = 'hello, Leiyu\n'  # 雷雨在这里输入了 字符串+ \n 
	>>> hellos = repr(hello)	# \n 本来代表换行的 但 repr() 这后 
	>>> print hellos	# 还是print 原样输出了
	'hello, Leiyu\n'
	>>> repr(hello)	# 这个 还是让 编译器去读的 雷雨读这个 比较别扭
	"'hello, Leiyu\\n'"	# 又是双引号 又是单引号的
	>>> 

#### 3 雷雨 接下来学习 制作 平方 立方 的表 or 类似矩阵形式

	>>> for x in range(1, 11): # 方式1
	...     print repr(x).rjust(2), repr(x*x).rjust(3),
	...     print repr(x*x*x).rjust(4)
	... 
	 1   1    1 # 这里是输出 直接在python中运行的
	 2   4    8
	 3   9   27
	 4  16   64
	 5  25  125
	 6  36  216
	 7  49  343
	 8  64  512
	 9  81  729
	10 100 1000
	
	>>> for x in range(1,10): # 方式 2
	...     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x) # 雷雨看到 这里的 str.format() 形式 恩 原来可以这样输出
	... 
	 1   1    1
	 2   4    8
	 3   9   27
	 4  16   64
	 5  25  125
	 6  36  216
	 7  49  343
	 8  64  512
	 9  81  729

看 这里 输出的 数字字符 自动 右对齐了 原来

- ==str.rjust() ==返回 str 自动右对其
- ==str.ljust()== 自动左对齐
- ==str.center()== 对中啦

然后看这里： ==str.zfill(n)==

	>>> '-3.1415'.zfill(10)
	'-0003.1415' # 自动fill 10位 -和 . 也算一位
	>>> '3.1415926'.zfill(5)
	'3.1415926'

#### 4 之后是  ==str.format()== 雷雨发现 原来 是这样使用的

	>>> print 'we are the {} who say "{}!"'.format('Knigths', 'Ni') # {} 来放 .format() 中的 一个 字符串
	we are the Knigths who say "Ni!"
	
	>>> print '{0} and {1}'.format('spam', 'eggs') # 注意{0} {1} 代表的 str 是社么
	spam and eggs
	
	>>> print '{1} and {0}'.format('spam', 'eggs') # 现在 雷雨晓得了 恩 {0} 是 spam
	eggs and spam
	
	>>> print 'this {food} is {adjective}.'.format(
	...     food='spam', adjective='absolutely horrble') # 还可以使用关键词
	this spam is absolutely horrble.

	>>> print 'the story of {0}, {1}, and {other}.'.format(
	...     'Bill', 'Leiyu', other='Jeremiah') # 还可以混合着来
	the story of Bill, Leiyu, and Jeremiah.

奥 还可以这样 使用 {!s} for str() , {!r} for repr() 和 {0:.5f} ：注意 ==:==

	>>> import math
	>>> print 'the value of PI is approximately {}.'.format(math.pi)
	the value of PI is approximately 3.14159265359.

	>>> print 'the value of PI is approximately {!r}.'.format(math.pi)
	the value of PI is approximately 3.141592653589793.

	>>> print 'The value of PI is approximately {0:.5f}.'.format(math.pi)
	The value of PI is approximately 3.14159.

恩 还可以这样玩：

	>>> dic = {'Sjored': 137, 'Jack':9801, 'Jeremiah': 9366} # 这里是一个 dictionary 
	>>> for name, phone in dic.items():
	...     print '{0:10} ===> {1:10d}'.format(name, phone) 
	... 
	Sjored     ===>        137 # 看这里是对其的哦
	Jeremiah   ===>       9366
	Jack       ===>       9801
	
	>>> print ('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};'
	...     'Jeremiah: {0[Jeremiah]:d}'.format(dic)) 
	Jack: 9801; Sjored: 137;Jeremiah: 9366 		# 这理还是少了一个空格 对不对 看下面
	
	>>> print ('Jack: {Jack:d}; Sjored: {Sjored:d};' # 这里最后一个 分号; 后没有空格 看 输出也是没有空格的
	...     'Jeremiah: {Jeremiah:d}'.format(**dic))
	Jack: 9801; Sjored: 137;Jeremiah: 9366

好了 雷雨今天的旅程就到这里

## 总

好啦  雷雨 今天学习了 

- str() 给人看的
- repr() 给编译器看的
- str.format() # 主要是这个的使用 输出

星期三, 11. 十一月 2015 11:29下午  1.5h



























