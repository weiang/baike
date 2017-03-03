#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest

from baike import *

#class TestBaikeExtractResume(unittest.TestCase):
#    def test_extract_resume(self):
#        pass
#
class TestBaikeExtractTime(unittest.TestCase):
    def test_extract_time_pattern1(self):
        test_set = [ 
                (u"1978年09月至1982年08月在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780900", "19820800"]),
                (u"1978年至1982年在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780000", "19820000"]),
                (u"中国人1978年09月21日至1982年08月15日在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780921", "19820815"]),
        ]
        for x in test_set:
            self.assertEqual(extract_time(x[0]), x[1]) 

    def test_extract_time_pattern2(self):
        test_set = [ 
                (u"1978.09至1982.08在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780900", "19820800"]),
                (u"1978至1982在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780000", "19820000"]),
                (u"中国人1978.09.21至1982.08.15在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780921", "19820815"]),
        ]
        for x in test_set:
            self.assertEqual(extract_time(x[0]), x[1]) 


#class TestBaikeExtractEntity(unittest.TestCase):
#    def test_extract_entity(self):
#        test_set = [
#            u"习近平于1978年至1982年在江苏省江苏工学院农业机械工程系农业机械专业学习，获工学学士学位"
#        ]
#        
#        for x in test_set:
#            r = extract_entity(x)
#            for k, v in r.items():
#                s = ""
#                for l in v:
#                    s += " ".join(l) + "\t"
#                # print "%s: %s" % (k, s)


class TestBaikeExtractResumeSingle(unittest.TestCase):
    def test_extact_resume_single(self):
        test_set = [
            u"习近平于1978年至1982年在江苏省江苏工学院农业机械工程系农业机械专业学习，获工学学士学位"
        ]

        baike = BaikePerson('test')
        for s in test_set:
            r = baike._extract_resume_single(s)

        cols = [r.post, r.enterprise, r.location, r.start_time, r.end_time]
        # print "%s" % ("\t".join(cols).encode('utf-8'))

class TestBaikePerson(unittest.TestCase):
    def test_structure(self):
        files = ["test.html", "test2.html"]
        for f in files:
            person = BaikePerson(f)


if __name__ == '__main__':
    unittest.main()
