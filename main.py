#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from baike import *

files = ["test.html", "test2.html"]

init_nlp_env()

for f in files:
    p = BaikePerson(f)
    s = p.to_json() 
    print s

destroy_nlp_env()
