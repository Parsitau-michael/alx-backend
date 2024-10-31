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

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds the maximum number of
        items, discard the most recently used item.

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(discarded_key))

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
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
