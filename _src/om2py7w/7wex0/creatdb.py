# -*- coding:utf-8 -*-
import sqlite3
import time

diary_tag = 'test'

"""t = time.time()
timestamp = int(t)
diary_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

diary_content = "this is save log print test"

data= (diary_tag, diary_date, diary_content)"""

# save into db
db_conn = sqlite3.connect('mydiary.db')
c = db_conn.cursor()
"c.execute('INSERT INTO diarys VALUES (?,?,?)', data)"

c.execute('SELECT * FROM diarys ORDER BY diary_date')
content = c.fetchall()
db_conn.close()

print type(content)
str_content = ("\n".join("%s,%s,%s" % tup for tup in content)).strip('()')

print str_content