# coding:utf-8
from bottle import Bottle, run
import sae

app = Bottle()

@app.route('/')
def hello():
    return 'hello, jeremiah -Bottle demo'

application = sae.create_wsgi_app(app)