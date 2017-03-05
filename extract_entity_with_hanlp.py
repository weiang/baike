#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import pdb

from jpype import *

from extract_time import *

HANLP_HOME_PATH = "/home/angwei/data/bin/Hanlp"
HANLP_LIB_PATH = HANLP_HOME_PATH + "/hanlp-1.2.8.jar"

HanLP = None

def init_nlp_env():
#    if isJVMStarted():
#        print "JVM already started"
#        return 
    global HanLP
    jvm_arg = "-Djava.class.path=%s:%s" % (HANLP_LIB_PATH, HANLP_HOME_PATH)
    startJVM(getDefaultJVMPath() , jvm_arg, "-Xms1g", "-Xmx1g")
    HanLP = JClass('com.hankcs.hanlp.HanLP')


def destroy_nlp_env():
    shutdownJVM()

entity_sub_class = [ 
        "n",
        "nr",
        "nrj",
        "nrf",
        "nr1",
        "nr2",
        "ns" # location
        "nsf",
        "nt", # organization 
        "ntc",
        "ntcf",
        "ntcb",
        "ntch",
        "nto",
        "ntu",
        "nts",
        "nth",
        "nn", # post
        "nnd"
]

entity_class = [
        "n",
        "ns",
        "nt",
        "nn",
        "ni",
        "nz",
        "v"
]

def extract_post(terms):
    result = []
    for term in terms:
        if term[1] == 0:
            continue
        t = term[0]
        if t.nature.startsWith("nn"):
            term[1] = 0
            result.append(t)

    r = [t.word for t in result]
    return "#".join(r)


def extract_enterprise(terms):
    result = []
    phrase = []
    for term in terms:
        if term[1] == 0:
            continue
        t = term[0]
        if t.nature.startsWith("nt") or t.nature.startsWith("nis") or t.nature.startsWith("nz") or t.nature.startsWith("ns"):
        # if t.nature.startsWith("n") and not t.nature.startsWith('nr'):
            term[1] = 0
            phrase.append(t)
        else:
            if len(phrase) != 0:
                result.append(phrase)
                phrase = []

    # last pharse
    if len(phrase) != 0:
        result.append(phrase)

    #pdb.set_trace()
    r = []
    for ts in result:
        s = "".join([t.word for t in ts])
        r.append(s)

    return "#".join(r)


def extract_location(terms):
    result = []
    flag = False
    for term in terms:
        t = term[0] 
        if term[1] != 0 and t.nature.startsWith("ns"):
            flag = True
            result.append(t)
            term[1] = 0
        else:
            if flag:
                break

    r = [t.word for t in result]
    return "".join(r)


def extract_entity(s):
    terms = HanLP.segment(s)
    r = [[term, 0] for term in terms] 

    for term in r:
        x = term[0]
        flag = False
        for c in entity_class:
            if x.nature.startsWith(c):
                flag = True
                term[1] = 1
                break

#    for t in r:
#        print "%s\t%d" % (t[0].toString().encode('utf-8'), t[1])

    location = extract_location(r)

#    print "#####"
#    for t in r:
#        print "%s\t%d" % (t[0].toString().encode('utf-8'), t[1])

    post = extract_post(r)

#    print "#####"
#    for t in r:
#        print "%s\t%d" % (t[0].toString().encode('utf-8'), t[1])

    enterprise = extract_enterprise(r)
#    print "#####"
#    for t in r:
#        print "%s\t%d" % (t[0].toString().encode('utf-8'), t[1])

    return (post, enterprise, location) 

def extract_resume_entity(s):
    start_time = ""
    end_time = ""
    r = extract_time(s)
    if r is not None:
        start_time = r[0]
        end_time = r[1]

    r = extract_entity(s)
    return (r[0].encode('utf-8'), r[1].encode('utf-8'), r[2].encode('utf-8'), start_time.encode('utf-8'), end_time.encode('utf-8')) 
