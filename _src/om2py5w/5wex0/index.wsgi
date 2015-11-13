# coding:utf-8
from bottle import *
import sae
import sys

app = Bottle()

@app.route('/')
@app.route('/write', method='GET')
def input_diary():

    if request.GET.get('save','').strip():
        diary_words = request.GET.get('words','').strip()
        diary_name = 'Diary.log' # if not exist then creat
        diary_file = open(diary_name, 'a+')
        diary_file.write(diary_words + '\n') # write words your
        diary_file.close()
        diary_file = open(diary_name, 'r')
        diary_content = diary_file.read()
        diary_file.close()
        return template('write_words.tpl', content=diary_content)

    else:
        diary_name = 'Diary.log'
        diary_file = open(diary_name, 'a+')
        diary_content = diary_file.read()
        diary_file.close()
        return template('write_words.tpl', content=diary_content)

application = sae.create_wsgi_app(app)