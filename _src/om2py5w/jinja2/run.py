#! /usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import Bottle, run, route, jinja2_template
import jinja2

app = Bottle()

@app.route("/")
def template_test():
    return jinja2_template('template.html', my_string='Wheeee!', my_list=[0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    app.run(host='localhost', port=8010, debug=True, reloader=1)