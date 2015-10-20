# 双推

## 背景 ##

在完成第一周任务的时候 每天code之后 push到github 与 gitbook中 都要使用：

	$ git push hub master 
	$ git push book master

来实现[双推](https://jeremiahzhang.gitbooks.io/pybeginner/content/toolssupport/gitbook.html) 有嫌麻烦 但是一直没去改变 程序员是需要精简的

触动 @小赖同学 在Issue中 发表 双推的代码 

嗯是该动起来 不能再每日都如上面上面一样的双推了

## 方案

根据 @小赖同学 提供的[stackoverflow问答](http://stackoverflow.com/questions/849308/pull-push-from-multiple-remote-locations) 去解决

1.使用：

	git remote set-url origin --push --add <a remote>
	git remote set-url origin --push --add <another remote>

2.修改 本地目录（local repo）中的.git/config

## 执行

1.从.git/config获得自己github与gitbook的远程库`ssh`或`http` url （每个github 远程库都有自己的url 每一本gitbook书籍也一样）因为之前已经设置了两个 remote ： hub （代表github中的remote repo）与 book （代表gitbook书籍 remote repo)

	[remote "hub"]
		url = git@github.com:JeremiahZhang/pybeginner.git
	[remote "book"]
	url = https://https://jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git

**注**apitoken在gitbook[用户设置](https://www.gitbook.com/@jeremiahzhang/settings)

2.根据`git remote set-url origin --push --add <a remote>` 添加 remote 设置 添加 gitbook remote repo `http` url to [hub]中（gitbook的`ssh`我没有尝试 因为之前实现[双推](https://jeremiahzhang.gitbooks.io/pybeginner/content/toolssupport/gitbook.html)的时候没有用）

	git remote set-url remote_name --push --add jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git

**注** remote_name 必须是我现有的 remote （此处我选择自己的remote为 `hub` ）可以在.git/config查看 也可以直接在git bash 中运行 git remote查看

添加之后 .git/config 中出现：

	[remote "hub"]
		url = git@github.com:JeremiahZhang/pybeginner.git
		fetch = +refs/heads/*:refs/remotes/hub/*
		pushurl = https://jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git
		
新增了 

	pushurl = https://jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git

3.以防万一 直接在hub中添加自己原先的ssh

	git remote set-url remote_name --push --add git@github.com:JeremiahZhang/pybeginner.git

同样.git/config的变化可查看：

	[remote "hub"]
	url = git@github.com:JeremiahZhang/pybeginner.git
	fetch = +refs/heads/*:refs/remotes/hub/*
	pushurl = jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git
	pushurl = git@github.com:JeremiahZhang/pybeginner.git

4.修改.git/config的 alias 【alias就是git 命令的 昵称或绰号】

	[alias]
		co = checkout
		ci = commit -m
		st = status
		br = branch
		pu = push hub master
		pl = pull
		ad = add --a
		hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
		type = cat-file -t
		dump = cat-file -p
		rf = reflog
5.修改本地文件内容 `git ad` `git ci`后 `git pu` 就实现双推 立即化简了上面 需要两次 `git push` 了

## 修改 ##

考虑到 hub 已经是一个 remote 名字 就修改 添加一个新的 remote origin

1-直接在.git/config中添加如下代码：

	[remote "origin"]
		pushurl = https://jeremiahzhang:apitoken@git.gitbook.com/jeremiahzhang/pybeginner.git
		pushurl = git@github.com:JeremiahZhang/pybeginner.git

2-[alias]中 修改push的绰号

	pu = push hub master

3-测试 git pu 成功

## 反思 ##

- DRP记住 不要重复我自己 所以当发现重复复杂的行为的时候 立即思考 搜索没有有精简的办法
- 其实一切以上只要修改.git/config文件中代码就行了 不过还是进行命令行的可操行和拓展性更强 就像之前群里说的160推
- 看看接下来能不能实现160推 。。。推 拓展 big picture

10/19/2015 9:51:59 PM 添加


	
	

