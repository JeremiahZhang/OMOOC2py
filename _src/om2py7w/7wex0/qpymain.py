# -*- coding: utf-8 -*-
#qpy:2
#qpy:webapp:Mydiary APP
#qpy://127.0.0.2:8000/
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

# diary function
def home():
    conn = sqlite3.connect('mydiary.db')
    c = conn.cursor()
    c.execute("CREATE TABLE diarys(diarytag text, diary_date text, diary_content text)")
    conn.commit
    c.close()
    return template(ROOT+'/home.html')
# webapp routers
app = Bottle()
app.route('/', method='POST')(home)
#app.route('/write', method='POST')(write)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)
try:
    server = MyWSGIRefServer(host="127.0.0.2", port="8000")
    app.run(server=server, reloader=False, debug=True)
except Exception,ex:
    print "Exception: %s" % repr(ex)