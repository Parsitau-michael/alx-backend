#!/usr/bin/env python3
"""Module that implements the LFU Cache Policy"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class definition"""
    def __init__(self):
        super().__init__()
        self.FreqList: Dict[str, int] = {}

    def put(self, key, item):
        """Adds key-value pairs to the cache keeping track of its frequency"""
        if key is None or item is None:
            return

        if key in self.FreqList:
            self.FreqList[key] = self.FreqList.get(key) + 1
            self.cache_data[key] = item
            return

        if len(self.FreqList) >= BaseCaching.MAX_ITEMS:
            LeastFreq = min(self.FreqList, key=self.FreqList.get)
            self.FreqList.pop(LeastFreq)
            self.cache_data.pop(LeastFreq)
            print("DISCARD: {}".format(LeastFreq))

        self.FreqList[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves key-value pairs from the cache tracking its frequency"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.FreqList:
            self.FreqList[key] = self.FreqList.get(key) + 1

        return self.cache_data[key]
