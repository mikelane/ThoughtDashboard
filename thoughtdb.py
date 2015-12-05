#!/usr/bin/env python3

"""
Thought Dashboard data handler
"""

__author__ = 'Mike Lane'

import json

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
    # tdb = Tdb("bad")
    tdb = Tdb("completeThunderData.json")
    print(tdb)
