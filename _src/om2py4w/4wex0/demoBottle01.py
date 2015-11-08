# coding=utf-8
from bottle import route, run, template

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/wiki/<pagename>')  #matches /wiki/Leraning Python
def show_wiki_page(pagename):
    pass

@route('/<action>/<user>')  # matches /follow/defnull
def user_api(action, user):
    pass

"""
def hello():
    return "Jeremiah Hello!"
"""
run(host='localhost', port=8080, debug=True)
# switched debug off for publich applocations