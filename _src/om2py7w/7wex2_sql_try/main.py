# -*- coding:utf-8 -*-
import sqlite3
conn = sqlite3.connect("example.db")
c = conn.cursor()

"""# create table
c.execute("CREATE TABLE stocks \
    (date text, trans text, symbol text, qty real, price real)")

# insert a row of data refer to the execute above
c.execute("INSERT INTO stocks Values ('2015-12-02', 'BUY', 'RHAT', 100, 35.14)")

# save or ci the changes
conn.commit()"""

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()

# close
conn.close()