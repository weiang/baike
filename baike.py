#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from collections import namedtuple
import json
import pdb 
import re

from nltk.tag import StanfordNERTagger
import jieba

from parse_baike import *

chinese_ner = StanfordNERTagger('chinese.misc.distsim.crf.ser.gz')


entity_class = {
        "PERSON": 0,
        "GPE": 1,
        "MISC": 2,
        "ORGANIZATION": 3,
        "O": 4
}

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


def extract_entity(s):
    tokens = list(jieba.cut(s))
    r = chinese_ner.tag(tokens) 
    
    entity_dict = {}
    pre_cls = ""
    terms = []
    for token, cls in r:
        # print type(token)
        print "%s, %s" % (token, cls)
        if cls != pre_cls:
            if pre_cls != "":
                entity_dict.setdefault(pre_cls, [])
                entity_dict[pre_cls].append(terms)
                terms = []
        terms.append(token)
        pre_cls = cls
            

    entity_dict.setdefault(cls, [])
    entity_dict[cls].append(terms)

    return entity_dict


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

class BaikePerson(Baike):
    def __init__(self, doc):
        self._doc = doc
        self._structure()

    def _structure(self):
        self._basic_info, resumes = extract_info(self._doc)
        print self._basic_info
        print resumes
        self._resumes = self._extract_resume_multi(resumes)
        print self._resumes
    
    def _extract_resume_single(self, sentence):
        post = ""
        enterprise = ""
        location = ""
        start_time = ""
        end_time = ""
        
        entity_dict = extract_entity(sentence)

        # start_time, end_time
        if 'MISC' in entity_dict:
            for terms in entity_dict['MISC']:
                r = extract_time(''.join(terms))
                if r is not None:
                    start_time = r[0]
                    end_time = r[1]
                    break
        
        # location
        if 'GPE' in entity_dict:
            s = ""
            for terms in entity_dict['GPE']:
                new_s = "".join(terms)
                if len(new_s) > len(s):
                    s = new_s
            location = s
        
        # enterprise
        if 'ORGANIZATION' in entity_dict:
            s = ""
            for terms in entity_dict['ORGANIZATION']:
                new_s = "".join(terms)
                if len(new_s) > len(s):
                    s = new_s
            enterprise = s
        
        return Resume(post, enterprise, location, start_time, end_time)

    def _extract_resume_multi(self, rs):
        results = []
        for r in rs:
            resume = self._extract_resume_single(r)
            print r.encode('utf-8')
            print "Resume:"
            keys = resume.__dict__.keys() 
            for k in keys:
                print "%s=%s, " % (k, getattr(resume, k).encode('utf-8'))
            print 
            results.append(resume)
        return results
    
    def to_json(self):
        pass
