#!/usr/bin/env python3

"""
Thought Dashboard data handler
"""

__author__ = 'Mike Lane'

import json, time
import pandas as pd
from hack_frame import list_parser

class Tdb:
    def __init__(self, filename):
        self.stories = []
        self.df = None
        self.filename = filename
        data = None
        try:
            with open(filename) as d:
                data = json.load(d)
            data = data['list']
            for item, d in data.items():
                self.stories.append(d)
            self.df = pd.DataFrame.from_dict(data, orient='index')
        except OSError as e:
            print(e)

    def get_weekly(self):
        r = {}
        for i in range(53):
            r[i] = []
        for story in self.stories:
            now = int(time.time())
            t = int(story['time_added'])
            if now - t < 31536000:
                t = time.gmtime(t)
                week = int(time.strftime("%U", t))
                r[week].append(story)
        return r

if __name__ == "__main__":
    # nltk.download()
    # tdb = Tdb("bad")
    tdb = Tdb("completeThunderData.json")
    r = tdb.get_weekly()
    # list_parser(tdb.stories)
    print(tdb)
