# coding:utf-8
from bottle import Bottle, request
import sae

app = Bottle()


application = sae.create_wsgi_app(app)