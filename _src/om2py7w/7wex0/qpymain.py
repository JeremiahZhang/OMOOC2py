# -*- coding: utf-8 -*-
#qpy:2
#qpy:webapp:Mydiary APP
#qpy://127.0.0.1:8081/
'''
Qpython webapp: Diary APP of @Jeremiah Zhang
Email: zhangleisuda@gmail.com
Version 1.0
'''
#  全局引用
import os
import sqlite3
from bottle import Bottle, ServerAdapter
from bottle import route, run, template, request, debug
import time

### 常量定义 ###
ROOT = os.path.dirname(os.path.abspath(__file__))

"""
由于默认的 bottle 在处理退出时比较难出来，
所以我们引入了自定义的 MyWSGIRefServer，
这能很好实现自我关闭
"""
### qpython web server ###
class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        #sys.stderr.close()
        import threading
        threading.Thread(target=self.server.shutdown).start()
        #self.server.shutdown()
        self.server.server_close()
        print "# QWEB"


### Build-in routers ###
def __exit():
    global server
    server.stop()

# 健康监测
def __ping():
    return "ok"

def _save_diary(data):
    # save into db
    db_conn = sqlite3.connect(ROOT + '/mydiary.db')
    c = db_conn.cursor()
    c.execute('INSERT INTO diarys VALUES (?,?,?)', data)
    db_conn.commit()
    db_conn.close()

def hist_diary():
    db_conn = sqlite3.connect(ROOT + '/mydiary.db')
    c = db_conn.cursor()
    c.execute('SELECT * FROM diarys ORDER BY diary_date')
    content = c.fetchall()
    db_conn.close()

    str_content = "\n".join("%s,%s,%s" % tup for tup in content) # unicode format
    return str_content

# webapp routers
app = Bottle()

@app.route('/')
@app.route('/home', method="GET")
def write():

    if request.GET.get('save','').strip():
        diary_tag = request.GET.get('tag')
        diary_content = request.GET.get('content')
        t = time.time()
        timestamp = int(t)
        diary_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        data= (diary_tag.decode('utf-8'), diary_date, diary_content.decode('utf-8'))
        _save_diary(data)
        history = hist_diary()
        return template(ROOT + '/home.html', log_content=history)
    else:
        history = hist_diary()
        return template(ROOT + '/home.html', log_content=history)

app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)
try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8081")
    app.run(server=server, reloader=True, debug=True)
except Exception,ex:
    print "Exception: %s" % repr(ex)