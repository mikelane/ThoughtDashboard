import nltk
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from collections import Counter


def excerpt_counter(excerpt):

    stop = stopwords.words('english')
    tokens = nltk.word_tokenize(excerpt)
    count_dict = Counter(tokens)
    for word in stop:
        count_dict.pop(word, None)
    return count_dict


def list_parser(tdb):
    totals = Counter({})
    i = 0
    for item in tdb:
        if 'excerpt' in item:
            totals += excerpt_counter(item['excerpt'])
        else:
            print(item)
    return totals


if __name__ == '__main__':

    list_parser(tdb)

