# -*- coding: utf-8 -*-
import sae
from bottle import *
from config import CFG

import xml.etree.ElementTree as ET

debug(True)
APP = Bottle()

@APP.get('/echo')
@APP.get('/echo/')
# def echo_wechat():  test setting wechat url
    # print request.query.keys()
    # print request.query.echostr
    # return request.query.echostr

# message wechat
@APP.post('/echo/')
def wechat_post():
    # print request.forms.keys()[0]
    xml = ET.XML(request.forms.keys()[0])
    fromUser = xml.findtext("")
    print xml.findtext("Content")