#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest

from baike import *

#class TestBaikeExtractResumeSingle(unittest.TestCase):
#    def setUp(self):
#        init_nlp_env()
#
#    def tearDown(self):
#        destroy_nlp_env()
#
#    def test_extact_resume_single(self):
#        test_set = [
#            u"习近平于1978年至1982年在江苏省江苏工学院农业机械工程系农业机械专业学习，获工学学士学位"
#        ]
#
#        baike = BaikePerson('test.html')
#        for s in test_set:
#            r = baike._extract_resume_single(s)
#
#        cols = [r.post, r.enterprise, r.location, r.start_time, r.end_time]
#        # print "%s" % ("\t".join(cols).encode('utf-8'))

class TestBaikePerson(unittest.TestCase):
    def setUp(self):
        init_nlp_env()
        pass

    def tearDown(self):
        destroy_nlp_env()
        pass

    def test_structure(self):
#        files = ["test.html", "test2.html"]
        files = ["test.html"]
        for f in files:
            person = BaikePerson(f)
            print person.to_json()

if __name__ == '__main__':
    unittest.main()
