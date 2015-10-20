# OMOOC.py 周任务代码试作

## 0w 日记交互系统

- py 调用
	- 拷贝 or clone 代码 [main.py](https://github.com/JeremiahZhang/pybeginner/blob/master/_src/om2py0w/0wex0/main.py) 到您的文件目录中 比如 `usr/om2py0w/0wex1/`
	- win 7 系统 Powershell 打开上面的文件目录 使用 `cd`
	- 执行 `python mian().py 我爱 python`
		+ pshell 第一行就打印 外部数据(关键字) `我爱 python`  
- CLI:
    + 交互
	    + 在上一步调用脚本 打印外部数据后 会显示脚本说明 请按着脚本说明进行
	    + 按住说明进行 日志写作（文件自动保存为txt格式） 每写完一行 回车进行下一行书写
	    + 如何结束？ 单行输入 `end`
	    + 会询问是否添加日期时间，请输入以下list中的任何一个英文字符或字符串 比如 `yes` 或者 `no` 
		    + 代表添加日期时间的string list： `yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']`
			+ 代表不添加日期时间string list： `no_list = ['no', 'n', 'NO', 'N']`
		+ 最后会打印你刚刚写作的所有内容（不包括时间）
		+ shell中打开文件 `cat diary_name.txt` 会打印日志内容
	+ 演示  
	![演示](https://raw.githubusercontent.com/JeremiahZhang/pybeginner/master/_image/05_readme_pre.JPG)
