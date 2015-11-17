#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

def help():
    """ # Welcome This is help doc:

    1. Quit Please Type : exit /q/quit/Q
    2. See Help Document Type: help/H/h/?
    3. See Diary Histroy Type: hist

    Let's Start. GO"""

def hist_logs():
    html_doc = requests.get('http://jeremiahzhang.sinaapp.com') # html_doc.text is the content of html
    soup = BeautifulSoup(html_doc.text) # html
    for item in soup.find_all('p'):
        print item.get_text()

def enter_tag(your_tag):
    tag_data = {'addtag': your_tag, 'save': 'save'}     # two input in write_words.tpl so you must add name='save' item
    requests.post('http://jeremiahzhang.sinaapp.com', data=tag_data)

def input_logs(your_log):
    log_data={'addtags': your_log, 'save': 'save'}
    requests.post('http://jeremiahzhang.sinaapp.com', data=log_data)

def main():

    print help.__doc__

    tag = raw_input('Type your tag:-->$')
    enter_tag(tag)

    while True:
        yourwords = raw_input('Type your words--->$')

        if yourwords in {'exit', 'q', 'quit','Q'}:
            sys.exit()
        elif yourwords in {'help', 'H','h','?'}:
            print help.__doc__
        elif yourwords == 'hist':
            hist_logs()
        else:
            input_logs(yourwords) # write new diarys or logs

if __name__ == '__main__':
    main()