# -*- coding:utf-8 -*-
from bottle import *
import sae

APP = Bottle()
application = sae.create_wsgi_app(APP)

@APP.get('/echo')
@APP.get('/echo/')
def echo_wechat():
    print request.query.keys()
    print request.query.echostr
    return request.query.echostr