# -*- coding: utf-8 -*-
import sae
from bottle import *
from config import CFG
debug(True)
APP = Bottle()

@APP.get('/echo')
@APP.get('/echo/')
def echo_wechat():
    print request.query.keys()
    print request.query.echostr
    return request.query.echostr

# message wechat
@APP.post('/echo')
def wechat_post():
    print request.forms.keys()