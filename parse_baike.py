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
import bs4

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


def extract_string_from_para(para):
#    anchors = para.find_all('a')
    s = ''.join(list(para.strings)).strip()
    return s


def extract_resume(soup):
    resumes = []
    
    # find main content
    main_content = soup.find('div', attrs={'class': 'main-content'})
    is_start = False
    for para in main_content.div.next_siblings:
        if para is None:
            continue
        if isinstance(para, bs4.element.NavigableString):
            continue
        if 'class' not in para.attrs:
            continue
        if para['class'] == ['anchor-list']:
            if is_start:
                break
            else:
                is_start = True
        if is_start:
            if 'class' not in para.attrs:
                continue
            if 'label-module' not in para.attrs:
                continue
            if para['class'] == ['para'] and para['label-module'] == 'para':
                s = extract_string_from_para(para)
                resumes.append(s)
    
    return resumes


def extract_info(file):
    with open(file, 'r') as fd:
        soup = BeautifulSoup(fd, 'html.parser')
        attrs = extract_basic_info(soup)
        resumes = extract_resume(soup)
    return (attrs, resumes)

        
def main():
    if len(sys.argv) != 2:
        print "Usage: %s <filename>" % (sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    attrs, resumes = extract_info(filename)    
    print attrs
    print resumes


if __name__ == '__main__':
    main()

