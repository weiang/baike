#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest

from extract_entity_with_hanlp import *

class TestBaikeExtractEntity(unittest.TestCase):
    def setUp(self):
        init_nlp_env()

    def tearDown(self):
        destroy_nlp_env()

    def test_extract_entity(self):
        test_set = [
            u"习近平于1978年至1982年在江苏省江苏工学院农业机械工程系农业机械专业学习，获工学学士学位",
            u"1968—1978 甘肃省地质局地质力学队技术员、政治干事、队政治处负责人",
            u"2002－2003年　河南省委书记、省长,兼任黄河防汛总指挥部总指挥",
            u"2002.07－2003.12河南省委书记、省长,兼任黄河防汛总指挥部总指挥",
            u"中国人1978年09月21日至1982年08月15日在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；"
        ]
        
        for x in test_set:
            r = extract_resume_entity(x)
            print "post=%s, enterprise=%s, location=%s, start_time=%s, end_time=%s" % (r[0].encode('utf-8'), r[1].encode('utf-8'), r[2].encode('utf-8'), r[3].encode('utf-8'), r[4].encode('utf-8'))

if __name__ == '__main__':
    unittest.main()
