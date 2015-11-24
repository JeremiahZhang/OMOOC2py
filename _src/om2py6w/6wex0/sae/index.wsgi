# -*- coding:utf-8 -*-
from bottle import *
import sae

import config
from web import APP

application = sae.create_wsgi_app(APP)