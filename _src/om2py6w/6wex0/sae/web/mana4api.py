# -*- coding: utf-8 -*-
import sae
from bottle import *
from config import CFG
import time

import xml.etree.ElementTree as ET

import hashlib
import sae.kvdb

count = 0

KV = sae.kvdb.KVClient()

debug(True)
APP = Bottle()

def _help():
    ''' # 是也乎, 俺是极简帮助文档:
    - 1 查看俺 输入 h
    - 2 想输入笔记 按这样的格式 {n:这是我的笔记}
            注意 不包括{}
    - 3 想看你输入的所有历史笔记 请输入 hist
    '''

def _save_note(userid, note):
    global count
    count += 1

    notekey = 'note' + str(count)       # 不同时刻笔记 set 字典中的key one by one
    usr = KV.get(userid)
    usr[notekey] = note
    KV.replace(userid, usr)

def _hist_note(userid):
    result = []
    usr = KV.get(userid)        # 返回字典是无序的
    sorted_usr = sorted(usr)  # sorted  is list en
    for key in sorted_usr:
        v = usr[key]
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
    tStamp = time.time()

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
        elif "i" == __Content:
            uid = hashlib.sha1(toUser).hexdigest()      # add security
            print uid
            usr = KV.get(uid)
            print type(usr)
            if None == usr:
                # 首次应答,没有建立档案
                KV.set(uid, {'tag':'null', 'note':'null'})
                content = "建立档案\n输入你的标签如\n tag:心情"
            else: # have usr doc
                if "tag" in usr.keys():
                    # have usr email
                    content = "你的标签: {}".format(usr['tag'])
                else:
                    # there is no usr email
                    content = "请输入你的标签如\ntag:心情"
            print CFG.TPL_TEXT% locals()
            return CFG.TPL_TEXT% locals()
        elif "tag" in __Content.split(":"):
            uid = hashlib.sha1(toUser).hexdigest()
            usr = KV.get(uid)
            print type(usr)
            print usr
            print __Content[3:]
            usr['tag'] = __Content[4:]
            KV.replace(uid, usr)
            content = "你的标签: {}".format(usr['tag'])
            print CFG.TPL_TEXT% locals()
            return CFG.TPL_TEXT% locals()
        elif "n" in __Content.split(":"):
            uid = hashlib.sha1(toUser).hexdigest()
            note_str = __Content[2:]

            _save_note(uid, note_str)
            content = "已经存入:-)"
            return CFG.TPL_TEXT% locals()
        elif "hist" == __Content:
            uid = hashlib.sha1(toUser).hexdigest()

            content = _hist_note(uid)

            return CFG.TPL_TEXT% locals()
    return None

    # print xml.findtext("Content")