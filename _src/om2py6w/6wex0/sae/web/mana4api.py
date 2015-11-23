# -*- coding: utf-8 -*-
import sae
from bottle import *
from config import CFG
import time

import xml.etree.ElementTree as ET

import hashlib
import sae.kvdb

KV = sae.kvdb.KVClient()

debug(True)
APP = Bottle()

"""
# test setting url in wechat API
@APP.get('/echo')
@APP.get('/echo/')
def echo_wechat():
    print request.query.keys()
    print request.query.echostr
    return request.query.echostr
"""

# message wechat
@APP.post('/echo/')
def wechat_post():
    # print request.forms.keys()[0] # get  xml message from wechat setdata
    xml = ET.XML(request.forms.keys()[0])
    fromUser = xml.findtext("ToUserName")
    toUser = xml.findtext("FromUserName")
    __MsgTpye = xml.findtext("MsgType")
    __Content = xml.findtext("Content")
    tStamp = time.time()

    if "text" == __MsgTpye:
        if "h" == __Content:
            content = "HalleluJa! Welcome!是也乎!"      # parameters should be the same in CFG.TPL_TEXT
            # print CFG.TPL_TEXT% locals()                    # in sae debug can print
            return CFG.TPL_TEXT% locals()                  # Use CFG in config.py, post to wechat
        elif "i" == __Content:
            uid = hashlib.sha1(toUser).hexdigest()      # add security
            print uid
            usr = KV.get(uid)
            print usr
            if None == usr:
                # 首次应答,没有建立档案
                KV.set(uid, {'em':'address'})
                content = "建立档案\n输入你的邮箱如\nem:foo@bar.com"
                pass
            else: # have usr doc
                if "em" in usr.keys():
                    # have usr email
                    content = "你的邮箱: {}".format(usr['em'])
                else:
                    # there is no usr email
                    content = "请输入你的邮箱如\nem:foo@bar.com"
            print CFG.TPL_TEXT% locals()
            return CFG.TPL_TEXT% locals()
        elif "em" in __Content.split(":"):
            uid = hashlib.sha1(toUser).hexdigest()
            usr = KV.get(uid)
            print type(usr)
            print usr
            print __Content[3:]
            usr['em'] = __Content[3:]
            KV.replace(uid, usr)
            content = "你的邮箱: {}".format(usr['em'])
            print CFG.TPL_TEXT% locals()
            return CFG.TPL_TEXT% locals()

    return None

    # print xml.findtext("Content")