# coding=utf-8
from bottle import *
import sys

@route('/')  # here you can type http://localhost:8010 to see myDiary.log
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

@route('/write', method="GET")
def input_diary():

    if request.GET.get('save','').strip():
        diary_words = request.GET.get('words','').strip()
        diary_name = 'Diary.log' # if not exist then creat
        diary_file = open(diary_name, 'a+')
        diary_file.write(diary_words + '\n')
        diary_file.close()
        return template('write_words.tpl', content=diary_words)

    else:
        diary_name = 'Diary.log'
        diary_file = open(diary_name, 'r')
        diary_content = diary_file.read()
        diary_file.close()
        return template('write_words.tpl', content=diary_content)

if __name__ == '__main__':
    run(host='localhost', port=8010, debug=True, reloader=1) # switched debug off for publich applocations