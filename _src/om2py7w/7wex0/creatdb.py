# -*- coding:utf-8 -*-
import sqlite3
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


conn = sqlite3.connect(ROOT+'/mydiary.db')
c = conn.cursor()
c.execute("CREATE TABLE diarys(diarytag text, diary_date text, diary_content text)")
conn.commit
c.close()