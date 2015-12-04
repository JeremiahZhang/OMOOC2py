#-*- coding:utf-8 -*-
#qpy:2
#qpy:webapp:Sample
#qpy://localhost:8080/
"""
This is a sample for qpython webapp
"""
import os.path
from bottle import Bottle, ServerAdapter
from bottle import template,request,response,redirect,HTTPResponse
root = os.path.dirname(os.path.abspath(__file__))

import androidhelper
Droid = androidhelper.Android()
Droid.startLocating(5000,5)

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
        self.server.server_close() #<--- alternative but causes bad fd exception
        print "# qpyhttpd stop"

def __exit():
    Droid.stopLocating()
    global server
    server.stop()

def __ping():
    return "ok"


def index():
    Droid.vibrate()
    return """<html><body><button onclick='location.href="/hello"'>显示我在哪里</button></body></html>"""

def hello():
    location = Droid.getLastKnownLocation().result
    location = location.get('network', location.get('gps')) # you should open gps in your phone or it will NoneType
    # location = {"latitude":"116.387884","longitude":"39.929986"}
    return template(root+'/baidu.tpl',lat=location['latitude'],lng=location['longitude'])

if __name__ == '__main__':
    app = Bottle()
    app.route('/', method='GET')(index)
    app.route('/hello', method='GET')(hello)
    app.route('/__exit', method=['GET','HEAD'])(__exit)
    app.route('/__ping', method=['GET','HEAD'])(__ping)

    try:
        server = MyWSGIRefServer(host="127.0.0.1", port="8080")
        app.run(server=server,reloader=False)
    except Exception,ex:
        print "Exception: %s" % repr(ex)