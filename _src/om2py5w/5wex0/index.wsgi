# coding:utf-8
from bottle import *
import sae
app = Bottle()

@app.route('/')
def index():
    return template('hello', hello='jeremiah go')

application = sae.create_wsgi_app(app)