#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

html_doc = requests.get('http://localhost:8010/') # html_doc.text is the content of html
soup = BeautifulSoup(html_doc.text, 'html.parser') # html
soup_textarea = soup.textarea # TYPE is list
textarea_contents_str = soup_textarea.contents[0]
print textarea_contents_str