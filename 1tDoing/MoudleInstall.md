# Python Package Install

## 背景 ##

有一个微信公众号 每次写点内容 总要输入密码 浏览器记录了也没有用   
所以想写一个python脚本 直接调用 登录微信公众号网页[https://mp.weixin.qq.com/](https://mp.weixin.qq.com/)

## 探索

- 经过 Google Search [http://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python](http://stackoverflow.com/questions/2910221/how-can-i-login-to-a-website-with-python) 要安装 automating Web browsing Package [twill](http://twill.idyll.org/)
	+ 根据 [easy install](http://peak.telecommunity.com/DevCenter/EasyInstall#downloading-and-installing-a-package) 安装 twill 不行啊
	+ 不知其他package行不行 还待验证
- 居然没有直接去 the Python Package Index [PyPI](https://pypi.python.org/pypi)网页去找 **教训**
- 醒悟过来后 找到[twill-1.8.0](https://pypi.python.org/pypi/twill)
- 安装遇到问题 回归 help文档 Installing Python Modules

## 安装 ##

### 方案-1 ###

在[PyPI](https://pypi.python.org/pypi)下载对应的Package 一般package 有说明怎么安装 安装说明来也可以  
但是也可以下载 package 使用python进行安装

- 从PyPI下载Packege文件 如[twill-1.8.0](https://pypi.python.org/pypi/twill) gar.gz文件到目录C:\temp
- 解压package压缩包 可以在文件目录中 `C:\temp\twill-1.8.0` 有个setup.py脚本
- 使用Python安装 (window Powershell中)

		C:\temp\twill-1.8.0
		python setup.py install
可以成功安装

### 方案-2 ###

若在PyPI中的package有安装说明 就直接用command line安装

## 总 ##

- 需求外部 python package
- 直接从PyPI中寻找Package
	- 若直接有安装说明 就用cmd line命令安装
- 下载压缩文件 解压 
- 安装 window shell中 `python setup.py install` 安装

10/20/2015 10:06:09 PM
