# coding:utf-8
from bottle import *
import sae
app = Bottle()

@app.route('/')
def write():
    return template('hello', hello='Haliluja Fancer', content='test')

@app.route('/', method='POST')
def continu_write():
    content = request.forms.get('txtadd')
    return template('hello', hello='Haliluja Fancer', content=content)

application = sae.create_wsgi_app(app)