#-*-coding:utf8;-*-
#qpy:console
#Author:QPython Developer <http://qpython.org>
#
import urllib2
import androidhelper
import web
import socket
urls = (
    '/location/(.*)', 'location',
    '/(.*)', 'hello'
)

App = web.application(urls, globals())
Droid = androidhelper.Android()
localIP = socket.gethostbyname(socket.gethostname())
externalIP = '0.0.0.0'

class hello:        
    def GET(self, name):
        Droid.vibrate() # tell self that some one was access
        Droid.makeToast("User <%s> vist Home" % web.ctx.ip)
        return "<html><body>Hello from my phone, You can <a href='/location/'>follow my location</a> : )</body></html>"

class location:        
    def GET(self, name):
        Droid.vibrate() # tell self that some one was access
        Droid.makeToast("User <%s> visit Location" % web.ctx.ip)
        location = Droid.getLastKnownLocation().result
        location = location.get('network', location.get('gps'))

        return "<html><body><a href='/'>Back to Homepage</a><br /><br /><h3>I am here</h3><img src='http://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=12&size=400x400&sensor=false&markers=color:green|label:I|%s,%s' /></body></html>" % (location['latitude'],location['longitude'],location['latitude'],location['longitude'])



if __name__ == "__main__":
    info = "Web Server serve at (%s:%s)" % (externalIP,'8080')
    Droid.makeToast(info)

    App.run()
