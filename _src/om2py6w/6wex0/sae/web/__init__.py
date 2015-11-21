# -*- coding: utf-8 -*-
from bottle import *

APP = Bottle()
APP.mount('/api', __import__('mana4api').APP)