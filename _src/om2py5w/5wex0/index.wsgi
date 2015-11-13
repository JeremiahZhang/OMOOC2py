# coding:utf-8
VERSION = 'Jeremiah v15.11.13'
from bottle import Bottle, request
import sae
import urllib2 as urilib

app = Bottle()

@app.route('/')
def hello():
    return ''' %s powered by Bottle and SAT !
    usage:
    $ curl -d 'uri=http://sina.com' 1.jeremiahzhang.sinaapp.com/write/
        ''' % VERSION

@app.route('/write', method='POST')
def write():
    uri = request.form.get('uri')
    print uri
    result = askCloud(APITYPE, uri)
    return '/wirte %s' % result

application = sae.create_wsgi_app(app)