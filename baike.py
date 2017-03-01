#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from collections import namedtuple
import pdb 
import re

class BaikeException(Exception):
    pass


class Baike(object):
    pass


Resume = namedtuple("Resume", ['post', 'enterprise', 'province', 'city', 'start_time', 'end_time'])

time_patterns = [
        "\d+年(\d+月)?(\d+日)?",
        "\d+(.\d+)?(.\d+)?"
]


def normalize_time(ds):
    chars = ["年", "月", "日", "."]
    r = ds
    for c in chars:
        r = r.replace(c, "")

    # pad zeros
    zeros = (8 - len(r)) * '0'
    return r + zeros


def extract_time(s):
    for p in time_patterns:
        r = [] 
        rs = re.finditer(p, s)
        for d in rs:
            ds = normalize_time(d.group())
            r.append(ds)
        if len(r) == 2:
            return r

    return None


class BaikePerson(Baike):
    def __init__(self, doc):
        self._doc = doc
        self._structure()

    def _structure(self):
        with open(self._doc) as fd:
            pass
    
    def _extract_resume_single(self, sentence):
        post = ""
        enterprise = ""
        province = ""
        city = ""
        start_time = ""
        end_time = ""
        
        return Resume(post, enterprise, province, city, start_time, end_time)
