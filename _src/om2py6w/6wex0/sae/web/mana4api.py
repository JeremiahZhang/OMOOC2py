# -*- coding: utf-8 -*-
import sae
from bottle import *
from config import CFG
import time

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
    # print request.forms.keys()[0] # get  xml message from wechat setdata
    xml = ET.XML(request.forms.keys()[0])
    fromUser = xml.findtext("ToUserName")
    toUser = xml.findtext("FromUserName")
    __MsgTpye = xml.findtext("MsgType")
    __Content = xml.findtext("Content")
    if "text" == __MsgTpye:
        if "h" == __Content:
            tStamp = time.time()
            content = "Haliluya! Welcome!是也乎!"
            print CFG.TPL_TEXT% locals()                    # in sae debug can print
            return CFG.TPL_TEXT% locals()                  # Use CFG in config.py, post to wechat
    # print xml.findtext("Content")