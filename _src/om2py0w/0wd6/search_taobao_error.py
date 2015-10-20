# -*- coding: utf-8 -*-
# 在win shell 中 无法打开
import os
import sys

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
url = url[:-1]
os.system.open(url)