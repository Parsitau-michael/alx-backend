#!/usr/bin/python3
"""
MRUCache class implementing a Most Recently Used (MRU) caching algorithm.
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class implementing a Most Recently Used (MRU) caching algorithm.
    """
    def __init__(self):
        """
        Initialize the MRUCache instance.
        """
        super().__init__()
        self.recent = []

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum number of
        items, discard the most recently used item.

        """
        if key is None or item is None:
            return

        if key in self.recent:
            self.recent.remove(key)

        if len(self.recent) >= BaseCaching.MAX_ITEMS:
            discard = self.recent[-1]
            self.recent.remove(discard)
            self.cache_data.pop(discard)
            print("DISCARD: {}".format(discard))

        self.recent.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key associated with the item to be retrieved.

        Returns:
            The item if found in the cache, or None if the key is not present
            or if the key is None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.recent.remove(key)
        self.recent.append(key)
        return self.cache_data[key]
