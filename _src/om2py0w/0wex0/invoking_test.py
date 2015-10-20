# -*- coding: utf-8 -*-
import sys
reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8')
print ('我爱python'.encode(sys.stdout.encoding))
keywords = sys.argv[:]
for words in keywords:
    print words,