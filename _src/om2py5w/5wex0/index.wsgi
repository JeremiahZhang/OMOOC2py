# coding:utf-8
from bottle import *
import sae
app = Bottle()

@app.route('/')
def index():
    return template('hello', hello='Haliluja Fancer', content='test')

@app.route('/add', method='POST')
def add():
    cnt = request.forms.get('txtadd')

application = sae.create_wsgi_app(app)