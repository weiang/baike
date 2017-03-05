#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from collections import namedtuple
import json
import pdb 
import re

from parse_baike import *
#from extract_entity_with_nltk import *
from extract_entity_with_hanlp import *


class BaikeException(Exception):
    pass


class Baike(object):
    def __init__(self):
        self.attrs = {}

    def serialize():
        return json.dumps(self.attrs) 
        raise BaikeException("Not Implemented")

    def __getattr__(self, name):
        if name not in self.attrs:
            self.attrs[name] = ""
        return self.attrs[name]


Resume = namedtuple("Resume", ['post', 'enterprise', 'location', 'start_time', 'end_time'])

def is_empty_resume(resume):
    r = True
    for k,v in resume.__dict__.items():
        if v != "":
            r = False
            break
    return r


def resume2dict(resume):
    r = {}
    for k, v in resume.__dict__.items():
        r[k] = v
    return r


class BaikePerson(Baike):
    def __init__(self, doc):
        self._doc = doc
        self._structure()

    def _structure(self):
        self._basic_info, resumes = extract_info(self._doc)
        #print self._basic_info
        #print resumes
        self._resumes = self._extract_resume_multi(resumes)
        #print self._resumes
    
    def _extract_resume_single(self, sentence):
        entities = extract_resume_entity(sentence) 
        return Resume(*entities)

    def _extract_resume_multi(self, rs):
        results = []
        for r in rs:
            resume = self._extract_resume_single(r)
            #print r.encode('utf-8')
            #print "Resume:"
            #keys = resume.__dict__.keys() 
            #for k in keys:
            #    print "%s=%s, " % (k, getattr(resume, k).encode('utf-8'))
            #print 
            if not is_empty_resume(resume):
                results.append(resume)
            else:
#                print "empty resume"
                pass
        return results
    
    def to_json(self):
        d = self._basic_info.copy() 
#        for k, v in d.items():
#            print k, v

        resumes = [] 
        for r in self._resumes:
            new_r = resume2dict(r)
            resumes.append(new_r)
        d['resume'] = resumes
#        for r in resumes:
#            for k,v in r.items():
#                print k,v
#            print "####"
        return json.dumps(d)
