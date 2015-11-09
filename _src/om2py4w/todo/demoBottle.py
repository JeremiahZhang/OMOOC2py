# coding=utf-8
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)

run(host='localhost', port=8080)




@get('/login') # or @route('/login')
def login():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="login" type="submit" />
            """

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


"""@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/wiki/<pagename>')  #matches /wiki/Leraning Python
def show_wiki_page(pagename):
    pass

@route('/<action>/<user>')  # matches /follow/defnull
def user_api(action, user):
    pass"""

"""
def hello():
    return "Jeremiah Hello!"
"""