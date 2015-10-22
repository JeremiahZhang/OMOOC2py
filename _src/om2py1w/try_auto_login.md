# 自动登录网页 #

## 背景 ##

- 实际需求：微信公众号网页每次登录需要密码 没有记住密码功能
- 想着写个脚本 调用 可自动登录

## 想法 ##

- 1.open the website through webbrowser like FireFox and Chrome
- 2.input user_name and password in python script to login the website

## 尝试 ##

- google到 twill 模块 [http://twill.idyll.org/](http://twill.idyll.org/) 发现花了笨功夫 
	- 没有仔细阅读twill文档 （笨功夫 需谨慎）
> twill is a simple language that allows users to browse the Web from a command-line interface.

- then 在stackoverflow上又有说requests模块
	- 简单浏览 requests 文档 也不是我所理想的[http://docs.python-requests.org/en/latest/#testimonials](http://docs.python-requests.org/en/latest/#testimonials)
- 发现姿势不对
	- then re-search got this [https://www.google.co.jp/search?q=open+browser+auto+login+python&ie=utf-8&oe=utf-8&gws_rd=cr&ei=U-EoVuTWJ4PpmAXo3IOADg](https://www.google.co.jp/search?q=open+browser+auto+login+python&ie=utf-8&oe=utf-8&gws_rd=cr&ei=U-EoVuTWJ4PpmAXo3IOADg)
	- got Selenium Client Driver [http://selenium-python.readthedocs.org/installation.html](http://selenium-python.readthedocs.org/installation.html)
		- [PiPY](https://pypi.python.org/pypi/selenium)

### 探索-开始挖硒 ###

