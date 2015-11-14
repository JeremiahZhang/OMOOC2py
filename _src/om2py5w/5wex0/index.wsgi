# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import *
import sae
import time
import sae.kvdb
import os

count = 0

kv = sae.kvdb.Client()

def _save_to_kvdb(post):
    global count
    count += 1

    logtime = time.ctime()
    key = 'key' + str(count)
    value = {'time':logtime, 'content':post}
    kv.set(key, value)          # 设置key的值为value

def _get_datainkvdb():
    results = []
    for item in kv.get_by_prefix('key'):
        results.append(item[1]) # get key's value
    return results

app = Bottle()

@app.route('/')
def write():
    mylog = _get_datainkvdb()   # get log history
    return template('write', hello='Hallelujah', log=mylog)

@app.route('/', method='POST')
def saveWrite():

    get_data = request.forms.get('txtadd')
    _save_to_kvdb(get_data)
    mylog = _get_datainkvdb()
    return template('write', hello='Hallelujah', log=mylog)

application = sae.create_wsgi_app(app)