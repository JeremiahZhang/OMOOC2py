# coding=utf-8
from bottle import route, run, static_file, template

@route('/')  # here you can type http://localhost:8080 to see myDiary.log
@route('/hello')
def hello():
    return "<h1>Dear Friend!<p>This is Your Diary Web! have fun!</p></h1>"

@route('/static/<filename>') # without the line 4 you must type http://localhost:8080/static/myDiary.log to brower can see myDiary.log file
def server_static(filename="myDiary.log"):
    return static_file(filename, root='/home/jeremiahzhang/OMOOC2py/_src/om2py4w/4wex0')

run(host='localhost', port=8080, debug=True, reloader=1)
# switched debug off for publich applocations