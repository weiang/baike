#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest

from extract_entity_with_nltk import *


class TestBaikeExtractEntity(unittest.TestCase):
    def test_extract_entity(self):
        test_set = [
            u"习近平于1978年至1982年在江苏省江苏工学院农业机械工程系农业机械专业学习，获工学学士学位"
        ]
        
        for x in test_set:
            r = extract_entity(x)
            for k, v in r.items():
                s = ""
                for l in v:
                    s += " ".join(l) + "\t"
                print "%s: %s" % (k, s)


if __name__ == '__main__':
    unittest.main()
