# 极简日志 公网版

APP部署于Sina SAE, 域名: http://jeremiahzhang.sinaapp.com/

- 网页端
	- ==tag here== 输入框中 键入 tag 回车
	- 网页显示过去日志
	- ==write== 输入框中 键入 你的日志
	- 问题:
		- tag 标签 暂时没有想出办法处理
		- 数据备份
- CLI
	- 在 runCLI.py 所在文件目录下 使用 python

		python runCLI.py

	- 待改进
		- 读取 History logs 的 url 得修改（需在服务端修改 index.wsgi
		- tag 分类管理尚未解决

- [代码](https://github.com/JeremiahZhang/OMOOC2py/tree/master/_src/om2py5w/5wex0) 
- [私人笔记](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week05_paas.html) 