#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import StanfordSegmenter
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import StanfordTokenizer


import jieba

def test_segmenter():
    segmenter = StanfordSegmenter(
            path_to_sihan_corpora_dict="/home/angwei/bin/stanford/stanford-segmenter/data/",
            path_to_model="/home/angwei/bin/stanford/stanford-segmenter/data/pku.gz",
            path_to_dict="/home/angwei/bin/stanford/stanford-segmenter/data/dict-chris6.ser.gz"
            )
#    segmenter = StanfordSegmenter()
    res = segmenter.segment(u"北海已成为中国对外开放中升起的一颗明星")
    print type(res)
    print res.encode('utf-8')

def test_tokenizer():
    tokenizer = StanfordTokenizer()
    sent = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks."
    print tokenizer.tokenize(sent)

def test_english_ner():
    eng_tagger = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    print eng_tagger.tag('Rami Eid is studying at Stony Brook University in NY'.split())


def test_chinese_ner():
    # sent = u'小明硕士毕业于中国科学院计算所后在日本京都大学深造'
    sent = u'习近平于1978年至1982年在江苏工学院农业机械工程系农业机械专业学习，获工学学士学位'
    tokens = jieba.cut(sent)
    new_tokens = []
    for x in tokens:
        print x
        new_tokens.append(x)

    new_sent = u" ".join(new_tokens)
    print new_sent
    chi_tagger = StanfordNERTagger('chinese.misc.distsim.crf.ser.gz')
    ## sent = u'北海 已 成为 中国 对外开放 中 升起 的 一 颗 明星'
    for word, tag in chi_tagger.tag(new_sent.split()):
        print word.encode('utf-8'), tag


def test_english_post():
    eng_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
    print eng_tagger.tag('What is the airspeed of an unladen swallow ?'.split())


def test_chinese_post():
    chi_tagger = StanfordPOSTagger('chinese-distsim.tagger')
    sent = u'北海 已 成为 中国 对外开放 中 升起 的 一 颗 明星'
    for _, word_and_tag in  chi_tagger.tag(sent.split()):
        word, tag = word_and_tag.split('#')
        print word.encode('utf-8'), tag


def test_english_parser():
    eng_parser = StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
    print list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split()))


def test_chinese_parser():
    sent = u'北海 已 成为 中国 对外开放 中 升起 的 一 颗 明星'
    chi_parser = StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz')
    print list(chi_parser.parse(sent.split()))


def main():
#    test_chinese_ner()
#    test_english_post()
#    test_chinese_post()
#    test_english_parser()
#    test_chinese_parser()
    test_segmenter()
#    test_tokenizer()

if __name__ == '__main__':
    main()
