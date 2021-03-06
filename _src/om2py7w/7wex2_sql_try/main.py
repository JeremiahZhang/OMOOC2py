# -*- coding:utf-8 -*-
import sqlite3
conn = sqlite3.connect("ex.db")
c = conn.cursor()

# create table
"""c.execute("CREATE TABLE stocks \
    (date text, trans text, symbol text, qty real, price real)")

# insert a row of data refer to the execute above
c.execute("INSERT INTO stocks Values ('2015-12-02', 'BUY', 'RHAT', 100, 35.14)")

# save or ci the changes
conn.commit()"""

"""# do this
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchone()"""

# Larger example that inserts many records at a time

purchases = [('2015-12-04', 'BUY', 'IBM', 1000, 45.00),
                      ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()

print '*'*10
print c.fetchall()
# close
conn.close()