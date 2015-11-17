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
        results.append(item[1])
    sort_results = sorted(results, key=lambda dict_value: dict_value['time'], reverse=True)
    return sort_results

app = Bottle()

@app.route('/')
def write():
    histlogs = _get_datainkvdb()
    return jinja2_template('layout.html', log=histlogs)

@app.route('/', method='POST')
def saveWrite():

    get_data = request.forms.get('addtext')
    _save_to_kvdb(get_data)
    newlog = _get_datainkvdb()
    return template('layout.html', log=newlog)

application = sae.create_wsgi_app(app)