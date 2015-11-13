# coding:utf-8
from bottle import *
import sae
import sys

app = Bottle()

@app.route('/')
@app.route('/write', method='GET')
def hello():
    return 'hello jeremiah-bottle demo'

application = sae.create_wsgi_app(app)