#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Qpython webapp: Diary APP CLI control of @Jeremiah Zhang
Email: zhangleisuda@gmail.com
Version 1.0
'''
import xml.etree.ElementTree as ET

TPL_TEXT=''' <xml>
<ToUserName><![CDATA[%(toUser)s]]></ToUserName>
<FromUserName><![CDATA[%(fromUser)s]]></FromUserName>
<CreateTime>%(tStamp)s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%(content)s]]></Content>
</xml>'''
