#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import re

from nltk.tag import StanfordNERTagger
import jieba

from extract_time import *

chinese_ner = StanfordNERTagger('chinese.misc.distsim.crf.ser.gz')

entity_class = {
        "PERSON": 0,
        "GPE": 1,
        "MISC": 2,
        "ORGANIZATION": 3,
        "O": 4
}


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


def extract_resume_entity(sentence):
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

    return (post, enterprise, location, start_time, end_time)

