#!/usr/bin/env python3

"""
Thought Dashboard data handler
"""

__author__ = 'Mike Lane'

import json, nltk
from hack_frame import list_parser

class Tdb:
    def __init__(self, filename):
        self.stories = []
        try:
            with open(filename) as d:
                data = json.load(d)
            data = data['list']
            for item, d in data.items():
                self.stories.append(d)
        except OSError as e:
            print(e)

    def __repr__(self):
        self.__str__()

    def __str__(self):
        for i in self.stories:
            print("{}".format(i))

if __name__ == "__main__":
    # nltk.download()
    # tdb = Tdb("bad")
    tdb = Tdb("completeThunderData.json")
    list_parser(tdb.stories)
    print(tdb)
