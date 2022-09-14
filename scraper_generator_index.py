#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:52:55 2022

@author: rafa
"""
from requests_html import requests

if __name__ == '__main__':
    src = 'https://www.youtube.com/watch?v=V74l_zS1x8E'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64"}
    response = requests.get(src, headers=headers)
    source = response.content
    response.close()
    source = source.decode(response.encoding)
    with open('index.html', 'w') as f:
        f.write(source)
