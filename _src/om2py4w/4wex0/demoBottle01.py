# coding=utf-8
from bottle import route, run, request, template

@route('/')  # here you can type http://localhost:8080 to see myDiary.log
@route('/hello')
def hello():
    return """
    <body>
        <h1>Dear Friend!</h1>
        <p>This is Your Diary Web! have fun!</p>

        <ul>
            <li>Read</li>
            <li>Write</li>
        </ul>
    </body>"""

@route('/read')
def read_diary():
    pass

@route('/write')
def write_diary():

    if request.GET.get('save','').strip():

        diary_words = request.GET.get('words','')

        diary_name = 'myDiary.log' # if not exist then creat
        diary_file = open(diary_name, 'a+')
        diary_file.write(diary_words + '\n')
        diary_file.close()

    else:
        return template('write_diary.tpl')

@route('/static/<filename>') # without the line 4 you must type http://localhost:8080/static/myDiary.log to brower can see myDiary.log file
def server_static(filename="myDiary.log"):
    return static_file(filename, root='/home/jeremiahzhang/OMOOC2py/_src/om2py4w/4wex0')

run(host='localhost', port=8080, debug=True, reloader=1)
# switched debug off for publich applocations