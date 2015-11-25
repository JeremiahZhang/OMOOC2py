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

def _help():
    ''' 是也乎, 俺是 极简日志交互 帮助文档:
    - 0 查看俺 输入 h
    - 1 想输入笔记 按这样的格式 {n:这是我的笔记}
    注意 不包括{}
    - 2 想看你输入的所有历史笔记 请输入 hist'''

def _save_note(userid, note, timestamp):

    notekey = timestamp         # 不同时刻笔记 set 字典中的key one by one
    note_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp)))
    usr = KV.get(userid)
    usr[note_time] = note
    KV.replace(userid, usr)

def _hist_note(userid):
    result = []
    usr = KV.get(userid)        # 返回字典是无序的
    sorted_usr = sorted(usr)  # sorted  is list then
    for key in sorted_usr:        # key is the time key in kvdb
        v = key + "\n" + usr[key]
        result.append(v)
    result_str = "\n".join(result)
    return result_str

# message wechat
@APP.post('/echo/')
def wechat_post():
    # print request.forms.keys()[0] # get  xml message from wechat setdata
    xml = ET.XML(request.forms.keys()[0])
    fromUser = xml.findtext("ToUserName")
    toUser = xml.findtext("FromUserName")
    __MsgTpye = xml.findtext("MsgType")
    __Content = xml.findtext("Content")
    tStamp = xml.findtext("CreateTime") # str timestampe convert to strtime need to int(tStamp)
    print type(tStamp)
    print tStamp

    if "text" == __MsgTpye:
        if "h" == __Content:
            content = _help.__doc__           # parameters should be the same in CFG.TPL_TEXT
            # print CFG.TPL_TEXT% locals()                    # in sae debug can print
            return CFG.TPL_TEXT% locals()                  # Use CFG in config.py, post to wechat
        elif "l" == __Content:
            content = "Would you like be my girlfriend? yes or no?"
            return CFG.TPL_TEXT% locals()
        elif "yes" == __Content:
            content = ":-) Thank God\nI finally find you."
            return CFG.TPL_TEXT% locals()
        elif "no" == __Content:
            content = ":-) Waiting you! :-) "
            return CFG.TPL_TEXT% locals()
        elif "n" in __Content.split(":"):
            uid = hashlib.sha1(toUser).hexdigest()
            usr = KV.get(uid)
            if None == usr:
                KV.set(uid, {})
                note_str = __Content[2:]
                _save_note(uid, note_str, tStamp)
            else:
                note_str = __Content[2:]
                _save_note(uid, note_str, tStamp)
            content = "已经存入:-)"
            return CFG.TPL_TEXT% locals()
        elif "hist" == __Content:
            uid = hashlib.sha1(toUser).hexdigest()
            content = _hist_note(uid)
            return CFG.TPL_TEXT% locals()
        else:
            content = _help.__doc__
            return CFG.TPL_TEXT% locals()
    return None

    # print xml.findtext("Content")