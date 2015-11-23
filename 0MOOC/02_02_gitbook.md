# Gitbook

## what
是什么

> GitBook是一个基于 [Node.js](https://nodejs.org/en/) 的命令行工具，可使用 Github/Git 和 [Markdown](http://baike.baidu.com/view/2311114.htm) 来制作精美的电子书，GitBook 并非关于 Git 的教程。

为什么

- 制作教程 教会半年前的自己 教是最好的学
- 获得反馈
- 可输出多种格式文件PDF epub mobi

## install

- Ubuntu14.04 折腾安装

	sudo apt-get update
	sudo apt-get install nodejs-legacy # 直接装nodejs会出现问题 但使用 $gitbook 时 error “/usr/bin/env: node: No such file or directory”
	sudo apt-get install npm
	sudo npm install -g gitbook-cli

参考 

- [Gitbook-cli](https://github.com/GitbookIO/gitbook-cli#how-to-install-it)  使用可以关注这个
- [Gitbook 安装](http://cowmanchiang.me/gitbook/gitbook/contents/install.html) 

## 现象

- gitbook 升级后, 关联 github 有问题

## 分析

- gitbook 服务升级, github 的 hook 没有对应升级
- 虽然增加了 [webhook](https://help.gitbook.com/github/index.html#webhooks) 但是还是出现 github与gitbook不同步现象 即 push to github 而 gitbook 没有对应改变 或者 改变较慢（当然自己自己目前发现 我的add webhook过程见 [webhook setup](https://jeremiahzhang.gitbooks.io/gitbookguide/content/build/webhookssetup.html)） 只能用double push **增补**
	+ push to github
	+ push to gitbook 

## 问题

- 多个仓库的自动化同步,官方不支持了.

## 方案

~ 作为不折腾会死星人,当然有姿势解决所有问题...

### 双推 double push *增补

所谓双推 就是将本地working directory(or我称其为Local Repo)的内容 即push到 Github 仓库 又推送到 Gitbook

#### 实现 ####

一推 github

- 我在Github Fork(相当于复制为我所用)[学员模板仓库](https://github.com/OpenMindClub/OMOOC.py) 我要基于该模板仓库建立自己学习开智编程课的教程 并改名为pybeginner 该远程库ssh为 `git@github.com:JeremiahZhang/pybeginner.git`
- 在我的电脑端本体建立文件目录（文件夹） 比如我建立的是名为pybeginner的文件夹（我称其为Local Repo 本地仓库）
	+ `git init` 初始化 以便与远程Repo连接
	+ `git remote add hub git@github.com:JeremiahZhang/pybeginner.git` 此处我将Local Repo与Github Repo远程仓库建立连接 这里hub是我定义Github repo的名字 而ssh值我add的是代表**Github上的pybeginner仓库**
	+ `git branch --track hub master`
	+ `git pull hub master` 以上将我的 github repo pybeginner拉回（传送 如星际迷航中的瞬间传送）本地local repo
		+ `git merge hub` [合并分支](https://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)
		+ `git br -d hub` 删除分支 hub
	+ 以后我只要在local repo编辑内容 再push 到github 就OK了
		+ 如 `git add README.md` 修改了README.md文件 通过 git add 添加到[staging area](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-Git-%E5%9F%BA%E7%A1%80#%E6%96%87%E4%BB%B6%E7%9A%84%E4%B8%89%E7%A7%8D%E7%8A%B6%E6%80%81)
		+ `git commit -m "modified README.md"` 提交到[git repository](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-Git-%E5%9F%BA%E7%A1%80#%E6%96%87%E4%BB%B6%E7%9A%84%E4%B8%89%E7%A7%8D%E7%8A%B6%E6%80%81)
		+ `git push -u hub master` 推到github

> 已经推到了Github这是一推	下面需要另一推才能形成二推

二推 gitbook

- Gitbook网页建立我的书籍 [Python Beginner Guide For Leiyu](https://www.gitbook.com/book/jeremiahzhang/pybeginner/details) 并找到 该书的 Git url 在书籍主页右下角 Setup 中 比如本书的git url为`https://git.gitbook.com/jeremiahzhang/pybeginner.git`
- $`git remote add book https://username:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git`  建立Local repo与gitbook repo的连接 其中username为gitbook的名称 apitoken是每个Gitbook账户特有的 可以在Account setting中找到 book为对应gitbook repo名字 可以自己命名的
- `git push -u book master` 将Local repo 推送到 gitbook

以上就是 双推 double push

## Disqus 评论 *增补

> gitbook 还支持许多插件，用户可以从 [NPM](https://www.npmjs.com/) 上搜索 gitbook 的插件，[gitbook 文档](https://github.com/GitbookIO/plugin) 推荐插件的命名方式为：
> 
- gitbook-plugin-X: 插件
- gitbook-theme-X: 主题
> 
所以，可以通过以上两种方式来搜索 gitbook 的插件或者主题

作为一个非常流行的为网站集成评论系统的工具，Gitbook可以集成Disqus 便于和读者进行交流 好形成反馈

- 1 首先注册Disqus 参考[配置 Disqus](https://openmindclub.gitbooks.io/omooc-py/content/support/Disqus_Setup.html) 
- 2 install disqus plugin   

	`$ npm install gitbook-plugin-disqus -g`
- 3 增加book.json文件 代码如下
 
		    {
			"plugins": ["disqus"],  
			"pluginsConfig": {  
			"disqus": {  
				"shortName": "XXXXXXX"  
					}
				}  
			}
- 效果
	- 在每一个页面都出现一下Disqus评论窗口

![disqus01](https://raw.githubusercontent.com/JeremiahZhang/gitbookguide/master/_images/disqus-01.JPG)

详细可参考我的 [折腾GitbookGuide](https://www.gitbook.com/book/jeremiahzhang/gitbookguide/details)

## 进展

- 150317 大妈创建
- 151007 雷雨增补