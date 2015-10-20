# -*- coding: utf-8 -*-
import sys, os, glob
# print sys.getdefaultencoding()
reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8')

current_dir = os.getcwd()
print type(current_dir)
os.chdir(current_dir)

for file in glob.glob("*.txt"):
    print(file)
    file_content = open(file, "r")
    print file_content.read()