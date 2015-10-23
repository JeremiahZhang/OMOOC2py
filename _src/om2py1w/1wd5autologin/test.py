# -*- coding: utf-8 -*-
import sys
reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8') # 默认编码

keywords = sys.argv[1:]
print type(keywords)  # list

print (sys.argv[0]) # str

your_keywords = sys.argv[1:]

for keywords in your_keywords:
    print keywords