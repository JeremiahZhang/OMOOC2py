# 极简日志 公网版

- python 应用在SAE上创建和部署
- bottle 如何和SAE结合 实现4w功能
- 实现公网访问
- KVDB 来收集 笔记 分类 管理 备份
- CLI 统计 看看

## python 应用在SAE上常见于部署

## bottle 和 SAE 结合

## 实现公网访问

[SAE git 代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#git) 

git init
git remote add sae https://git.sinacloud.com/jeremiahzhang
git add .
git commit -m 'beta 1.0 push'
git push sae master:1 # 部署到sae版本1

[git 设置 避免每次都要输入密码](https://help.github.com/articles/caching-your-github-password-in-git/) 