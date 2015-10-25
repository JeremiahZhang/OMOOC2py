# 自动登录网页 #

## 背景 ##

- 实际需求：微信公众号网页每次登录需要密码 没有记住密码功能
- 想着写个脚本 调用 可自动登录

----------

## 想法 ##

- 1.open the website through webbrowser like FireFox and Chrome
- 2.input user_name and password in python script to login the website

----------

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

----------

## 探索-开始挖硒 ##

- **安装** 因为在神奇的win 所以只能下载在本地目录 在本地目录使用

		python setup.py install
安装好库之后就开始实践了

### **实践-1 自动打开浏览器 进行google搜索** ###

代码： [go_google.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py1w/1wd5autologin/go_google.py)

		# -*- coding: utf-8 -*-
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys

		print """ Example 1:
    		==========
    
    		* open a new Firefox browser
    		* load the google homepage
    		* search for "github"
		"""

		browser = webdriver.Firefox()  			# 打开火狐浏览器
		browser.get("http://www.google.com")	# 打开url网页链接
		assert 'Google' in browser.title		# 确认是Google

		elem = browser.find_element_by_name('q') # 找到搜素栏 name = "q" 在google网页源码的 search field 
		elem.send_keys('github' + Keys.RETURN)   # 在搜索栏中输入输入关键字github后 执行搜索  Keys 相当于键盘keyboard
		# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
执行： 在shell中

		python go_google.py

效果：   
1.自动打开Firefox浏览器   
2.进入google主页   
3.自动键入关键字 gihub  
4.跳到搜索结果  

OK 这个你可以拓展下  
1.你可以输入外部数据  python go_google.py keyword01 keyword02  
2.....你可以继续构思呢


### 实践-2 登录facebook ###

代码：[go_facebook.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py1w/1wd5autologin/go_facebook.py)

    # -*- coding: utf-8 -*-
	from selenium import webdriver  			# 导入模块 
	from selenium.webdriver.support import ui
	from selenium.webdriver.common.keys import Keys

	def page_is_loaded(driver):					# 测试 网页是否加载好了
		return driver.find_element_by_tag_name("body") != None 

	driver = webdriver.Firefox()				# 启动FireFox浏览器
	driver.get("https://facebook.com/")			# 浏览器进入facebook页面

	wait = ui.WebDriverWait(driver, 10)			# 等待网页加载完毕
	wait.until(page_is_loaded)

	email_field = driver.find_element_by_id("email")  	# 找到facebook登录帐号栏
	email_field.send_keys("user_email@email.com") 		# 键入 user_email

	password_field = driver.find_element_by_id("pass")	# 找到facebook密码输入栏
	password_field.send_keys("your_password") 			# 键入 your password
	password_field.send_keys(Keys.RETURN)				# enter 确认
shell 执行

	python go_facebook.py
效果：  
1- 打开Firefox并   
2- 转到Fackbook页面   
3- 自动登录 facebook

### 实践3-登录微信公众号 ###

从上面facebook的例子 我可以解决我最初自动登录微信公众号的问题了

- 将 go_facebook.py 中的代码 改个url链接

		driver.get("https://mp.weixin.qq.com/")

- 改下email与password
- 但是你得注意 需要根据 [https://mp.weixin.qq.com/](https://mp.weixin.qq.com/) 网页源码 修改` email_field = driver.find_element_by_id("email")` `password_field = driver.find_element_by_id("pass")`这两处
	- 如何看网页源代码？你需要右击鼠标 点击`查看网页源代码`
	- 你需要确定 网页 `账户输入栏`的 `id` 与 `密码输入栏` 的 `id` 如在微信公众号网页源码中 你可以找到登录的源码

 <div class="login_frame">
                        <h3>登录</h3>
                        <div class="login_err_panel" style="display:none;" id="err"> </div>
                        <form class="login_form" id="loginForm">
                            <div class="login_input_panel" id="js_mainContent">
                                <div class="login_input">
                                    <i class="icon_login un"> </i>
                                    <input type="text" placeholder="邮箱/微信号/QQ号" id="account" name="account">
                                </div>
                                <div class="login_input">
                                    <i class="icon_login pwd"> </i>
                                    <input type="password" placeholder="密码" id="pwd" name="password" >
                                </div>
                            </div>
                            <div class="verifycode" style="display:none;" id="verifyDiv">
                                <span class="frm_input_box">
                                    <input class="frm_input" type="text" id="verify" name="verify" >
                                </span>
                                <img id="verifyImg" src="" />
                                <a href="javascript:;" id="verifyChange">换一张</a>
                            </div>
                            <div class="login_help_panel">
                                <label class="frm_checkbox_label" for="rememberCheck">
                                    <i class="icon_checkbox"></i>
                                    <input type="checkbox" class="frm_checkbox" id="rememberCheck">
                                    记住帐号
                                </label>
                                <a class="login_forget_pwd" href="/acct/resetpwd?action=send_email_page">无法登录？</a>
                            </div>
                            <div class="login_btn_panel">
                                <a class="btn_login" title="点击登录" href="javascript:" id="loginBt">登录</a>
                            </div>
                        </form>
                    </div>
其中 `账户输入栏` 部分源码：

	<div class="login_input">  
         <i class="icon_login un"> </i>  
         <input type="text" placeholder="邮箱/微信号/QQ号" id="account" name="account">
   	</div>
其中 id="account"
所以 改为 `email_field = driver.find_element_by_id("account")`

同理 `密码输入栏` 部分源码：

	<div class="login_input">
         <i class="icon_login pwd"> </i>
         <input type="password" placeholder="密码" id="pwd" name="password" >
    </div>
	
改为 `password_field = driver.find_element_by_id("pwd")`

经过修改之后 你可以参见代码 [go_wechat.py](https://github.com/JeremiahZhang/OMOOC2py/blob/master/_src/om2py1w/1wd5autologin/go_wechat.py)（只要修改一下你的账户与密码）执行 可自动登录 
 
这回你只要用shell调用 go_wechat.py脚本就可以自动微信公众号了 再也不用每次都要输入密码了 真cool

----------

## 拓展

- 你可以改为其他浏览器 selenium.WebDirver 支持 Firefox Chrome Ie and Remote
	- Currently supported WebDriver implementations are Firefox, Chrome, Ie and Remote
	- IE就算了吧 你尽量使用开源的
- 登入任何一个你想自动登入的网页 

----------

## 总 

- 你有没有发现什么是笨功夫了么？ 你在最初探索的时候 在twill上 因为没有认真看文档 漏了一个关键 就直接白花了近2个小时的时间 折腾在各种英文文档中
- 你的想法 尽量用英文 然后关键字 google search
- 你是不是还可以继续 比如登入芝麻星
	- 登录芝麻星 [http://beta.iomooc.com/](http://beta.iomooc.com/) 也是够烦的了
		+ 连接github 每次都显示白板 + 一行代码 然后刷新才能登录
	- 嗯 这回可以自动登录了
		- 这个已经解决 你只要注册账户
		- 简单修改脚本并调用
	- [x] 你已经完成了芝麻星的自动登录 代码[go_openmind.py]() 脚本完成 稍作简单修改
		- 修改网址
		- 修改用户名与密码
		- 增加寻找 login 按钮 然后 `enter` 如下

				login_field = driver.find_element_by_id("login")
				login_field.send_keys(Keys.RETURN)
 	- 如何不注册账户
		- 自动连接github
		- 登入
		- 这个你该如何解决呢？

# (￣▽￣) #

10/23/2015  
10/25/2015 5:22:21 PM 增加 go_openmind.py 自动登录芝麻星代码 
