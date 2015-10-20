# -*- coding: utf-8 -*-
# ref to https://wp-lai.gitbooks.io/learn-python/content/0MOOC/taobao.html
# 代码所在文件夹 进行命令行输入 python search_taobao.py keyword-1 keyword-2 ...
# win 可在 shell中使用
import sys
import webbrowser

keywords = sys.argv[1:] # argument from your keyword-1 and keywords-2 etc

url = "https://s.taobao.com/search?q="  # search url from taobao
for i in keywords:
    url += i + "+"
    print url
url = url[:-1] # remove the last "+"
webbrowser.open(url)
print "mission completed"