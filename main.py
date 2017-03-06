#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import os
import sys

from baike import *

def load_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            file_path = os.path.join(root, f)
            r.append(file_path)

        for d in dirs:
            dir_path = os.path.join(root, d)
            r.extend(load_files(dir_path))
    return r 

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <dir_name>" % (sys.argv[0])
        sys.exit(1)

    dir_name = sys.argv[1]
    files = load_files(dir_name)

    init_nlp_env()

    for f in files:
        p = BaikePerson(f)
        s = p.to_json() 
        print s

    destroy_nlp_env()

if __name__ == '__main__':
    main()
