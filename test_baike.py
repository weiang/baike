#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest

from baike import *

class TestBaikeExtractResume(unittest.TestCase):
    def test_extract_resume(self):
        pass

class TestBaikeExtractTime(unittest.TestCase):
    def test_extract_time_pattern1(self):
        test_set = [ 
                ("1978年09月至1982年08月在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780900", "19820800"]),
                ("1978年至1982年在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780000", "19820000"]),
                ("中国1978年09月21日至1982年08月15日在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780921", "19820815"]),
        ]
        for x in test_set:
            self.assertEqual(extract_time(x[0]), x[1]) 

    def test_extract_time_pattern2(self):
        test_set = [ 
                ("1978.09至1982.08在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780900", "19820800"]),
                ("1978至1982在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780000", "19820000"]),
                ("中国1978.09.21至1982.08.15.在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位；", ["19780921", "19820815"]),
        ]
        for x in test_set:
            self.assertEqual(extract_time(x[0]), x[1]) 


if __name__ == '__main__':
    unittest.main()
