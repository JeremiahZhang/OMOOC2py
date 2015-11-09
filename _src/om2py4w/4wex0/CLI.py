#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:8010/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

items = buffer.getvalue()
print (items)