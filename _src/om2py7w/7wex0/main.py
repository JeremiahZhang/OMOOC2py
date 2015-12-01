# -*- coding:utf-8 -*-
#qpy:2
#qpy:webapp:Sample
#qpy://localhost:8080/

from bottle import route, run

@route('/')
def hello():
    return "hello jeremiah zhang!"

run(host='localhost', port=8080, debug=1)