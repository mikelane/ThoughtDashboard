import nltk
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from collections import Counter


def excerpt_counter(excerpt):

    excerpt = excerpt.encode('ascii','ignore')
    stop = stopwords.words('english')
    tokens = nltk.word_tokenize(excerpt)
    new_tokens = [x.lower().strip() for x in tokens]
    count_dict = Counter(tokens)
    for word in stop:
        count_dict.pop(word, None)
    return count_dict


def list_parser(tdb):
    totals = Counter({})
    i = 0
    for item in tdb:
        e = ''
        if 'excerpt' in item:
            e += item['excerpt']
        if 'given_title' in item:
            e += ' ' + item['given_title']
        totals += excerpt_counter(e)
    return totals


if __name__ == '__main__':

    list_parser(tdb)


