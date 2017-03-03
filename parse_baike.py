#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: parse_baike.py
Author: angwei(angwei@baidu.com)
Date: 2017/03/03 18:35:24
"""

import sys

from bs4 import BeautifulSoup

def extract_basic_info(soup):
    attrs = {}

    bins = soup.find_all('dt', attrs={'class': 'basicInfo-item name'}) 
#    for bin in bins:
#        print bin
    
    bivs = soup.find_all('dd', attrs={'class': 'basicInfo-item value'})
#    for biv in bivs:
#        print biv

    r = {}
    for (key, value) in zip(bins, bivs):
        k = key.string.strip(": \t\n")
        v = value.string
        if v is None:
            x = value.find('a')
            v = x.string
        v = v.strip(": \t\n") 
        r[k] = v
    
    return r

def extract_resume(soup):
    resumes = []

    rs = soup.find_all('div', attrs={'class': 'para', 'label-module': 'para'})
    for r in rs:
        print r
    pass
    

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <filename>" % (sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    
    with open(filename, 'r') as fd:
        soup = BeautifulSoup(fd, "html.parser")
#        print extract_basic_info(soup)
        extract_resume(soup)


if __name__ == '__main__':
    main()

