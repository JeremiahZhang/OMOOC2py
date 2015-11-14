# coding:utf-8
from bottle import *
import sae
import time

def saveIntoFile(log_content):

    filename = 'sae_log.log'
    log_file_obj = open(filename, 'a+')
    log_file_obj.write(log_content + '\n')
    log_file_obj.close()

def addTime():
    log_time = time.ctime()
    return log_time

app = Bottle()

@app.route('/')
def write():
    return template('hello', hello='Haliluja Fancer', content='test')

@app.route('/', method='POST')
def saveWrite():

    content = request.forms.get('txtadd')
    return template('hello', hello='Haliluja Fancer', content=content)

application = sae.create_wsgi_app(app)