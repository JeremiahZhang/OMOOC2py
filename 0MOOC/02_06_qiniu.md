# 七牛云储同步

- Ubuntu 14.04 LTS

哈利路亚

## 背景

咦 雷雨的这次教程中图片 都放到了 Github 大妈提醒 放那里合适么

嗯 不合适 雷雨发现了云储 先用 七牛啦 [七牛](https://portal.qiniu.com/) 

## 使用

- 注册 可以用 Github 登录 
- 新建空间
- 直接上传图片 恩 然后使用外链 
	- 再使用 markdown 插入图片链接 就OK了

## 配置同步

- 下载文件 [命令行配置同步](http://developer.qiniu.com/docs/v6/tools/qrsync.html) 
- Ubuntu 下载 tar.gz 包
	- 直接解压即可
	- 在 /HOME 新建 qiniu 文件目录
	- 将解压文件 放入 qiniu 文件
- 恩 这里得配置 环境 添加路径 在.bash_profile 中 为了可以使用同步qrsync 之命令

		# for qiniu sync
		export PATH="$HOME/qiniu:$PATH"

	终端中：

		source .bash_profile # 在该文件目录下哦

- 建立 conf.json 放入 qiniu 文件夹

		{
		    "src":          "/home/jeremiahzhang/Pictures/ImgofBlog", # 这里是我的同步文件目录
		    "dest":         "qiniu:access_key=<AccessKey>&secret_key=<SecretKey>&bucket=<这放空间名 不要<>哦>",
		    "deletable": 0,
		    "debug_level":  1
		}

< AccessKey >  
< SecretKey >

以上两项 需要去7牛 获取

- 继续配置 在终端中

		chmod +x qrsync 

- 之后 你就可以 打开 qiniu文件 在该文件目录下 使用命令行

		qrsync conf.json # 进行同步

## o(∩∩)o

可以将图片直接用命令行同步到 七牛 螺

星期四, 12. 十一月 2015 10:13下午


	

	

	



