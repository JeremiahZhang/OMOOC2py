# 4w 日志交互web版

- Ubuntu14.04 LTS + 其自带终端
- SublimeText2 （ST2）
- Python 2.7.10
- Firefox 41.0.2 for Ubuntu

## web 端 网页访问
- python 运行：webserver.py 
	- 请将 write_words.tpl 保存在 与 webserver.py 同一个文件目录下
- 浏览器 访问：http://localhost:8010/write
	- text 中书写日志
	- text area 返回上一次输入内容
- 效果
![04webserverresult](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/04webserverresult.jpg) 

## CLI 交互

- python 运行 webserver.py
- python 运行 CLI.py
- 效果

![CLI07result.jpg](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/CLI07result.jpg) 


## 教程

- [教程](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week04_web_way.html)

## 代码

- [webserver.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py4w/4wex0/webserver.py)
- [CLI.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py4w/4wex0/CLI.py)
- [write_words.tpl](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py4w/4wex0/write_words.tpl)