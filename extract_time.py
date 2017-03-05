#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import re

time_patterns = [
        u"\d+年(\d+月)?(\d+日)?",
        u"[0-9]{1,4}(\.[0-9]{1,2})?(\.[0-9]{1,2})?"
]


def normalize_time(ds):
    # print ds
    chars = [u"年", u"月", u"日", u"."]
    r = ds
    for c in chars:
        r = r.replace(c, u"")

    # pad zeros
    zeros = (8 - len(r)) * '0'
    return r + zeros


def extract_time(s):
    # print s
    for p in time_patterns:
        r = [] 
        rs = re.finditer(p, s)
        for d in rs:
            ds = normalize_time(d.group())
            r.append(ds)
        if len(r) == 2:
            return r
    return None
