# -*- coding: utf-8 -*-
#qpy:2
#qpy:webapp:iMatch APP
#qpy://127.0.0.1:8080/
'''
Qpython webapp: iMatch
Email: zhangleisuda@gmail.com
Version 1.0
'''
#  全局引用
import os

from bottle import Bottle, ServerAdapter
from bottle import route, run, debug, template, error
from bottle import get, post, request, static_file
from bottle import jinja2_template

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
        print "# Qpython Imatch WebApp"

### Build-in routers ###
def __exit():
    global server
    server.stop()

# 健康监测
def __ping():
    return "ok"

### imatch main function set ###
# webapp routers
app = Bottle()

@app.route('/static/<filepath:path>') # Route static files such as images or CSS files
def serve_static(filepath):
    img_path = ROOT + "/image"
    return static_file(filepath, root=img_path)

@app.route('/')
@app.route('/index') # or @route('/upload')
def index():
    return jinja2_template('index.html')

@app.route('/pic1') # first + to add image
def pic1():
    return jinja2_template('upload1.html')

@app.route('/upload1', method='POST') # upload the image
def do_upload_pic1():
    category = "image"
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed!"

    save_path = ROOT + "/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return jinja2_template('showpic1.html', pic_item=upload.filename)

app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)
try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8080")
    app.run(server=server, reloader=True, debug=True)
except Exception,ex:
    print "Exception: %s" % repr(ex)