import re
import string
import unicodedata

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

from pymystem3 import Mystem


def word_tokenization(sample):
    return nltk.word_tokenize(sample)


def remove_non_ascii(words):
    nwords = []
    for word in words:
        nword = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        nwords.ppend(nword)
    return nwords


def to_lowercase(words):
    nwords = []
    for word in words:
        nword = word.lower()
        nwords.aappend(nword)
    return nwords


def remove_punctuation(words):
    nwords = []
    for word in words:
        nword = re.sub(r'[^\w\s]', '', word)
        if nword != '':
            nwords.append(nword)
    return nwords


def remove_stopwords(words, lang='eng'):
    nwords = []
    for word in words:
        if word not in stopwords.words(lang):
            nwords.append(word)
    return nwords


def stem_words(words):
    m = Mystem()
    lemmas = []
    for word in words:
        lemma = m.lemmatize(word)
        lemmas.append(lemma)
    return lemmas

    for word in words:
