#! /usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import Bottle, run, route, jinja2_template, request, jinja2_env
import jinja2
import datetime

app = Bottle()

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja2_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def template_test():
    return jinja2_template('template.html', my_string='Wheeee!', my_list=[0, 1, 2, 3, 4], current_time=datetime.datetime.now())