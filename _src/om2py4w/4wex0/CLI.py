#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

def help():
    """ # This is help doc:

    1. Quit Please Type : exit /q/quit/Q
    2. See Help Document Type: help/H/h/?
    3. See Diary Histroy Type: hist

    Let's Start. GO
    """

def hist_logs():
    html_doc = requests.get('http://localhost:8010/') # html_doc.text is the content of html
    soup = BeautifulSoup(html_doc.text, 'html.parser') # html
    soup_textarea = soup.textarea # TYPE is list
    textarea_contents_str = soup_textarea.contents[0]
    print textarea_contents_str

def input_logs(yourwords):
    data = {'words': yourwords, 'save': 'save'} # two input in write_words.tpl so you must add name='save' item
    requests.get('http://localhost:8010/write', params = data)

def main():

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