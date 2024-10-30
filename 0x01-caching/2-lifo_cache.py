#!/usr/bin/python3
"""
This module provides an implementation of a caching system called `LIFOCache`,
which follows the Last-In-First-Out (LIFO) eviction policy. When the cache
exceeds the defined limit (`MAX_ITEMS`), the most recently added item
is discarded.

Classes:
    LIFOCache -- a cache system that evicts the most recently added item
                 when reaching the maximum cache size.
Usage Example:
    cache = LIFOCache()
    cache.put("A", "Apple")
    cache.put("B", "Banana")
    cache.put("C", "Cherry")
    cache.put("D", "Date")  # This will discard "C"
    print(cache.get("C"))    # Output: None
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class

    This class implements a caching system with a Last-In-First-Out (LIFO)
    eviction policy. When the number of items in the cache exceeds `MAX_ITEMS`,
    the most recently added item is removed to make space for new items.

    Methods:
        put(key, item) -- Adds an item to the cache. If the cache exceeds the
                          limit, the most recently added item is removed.
        get(key) -- Retrieves an item from the cache by key.
    """
    def __init__(self):
        """
        Initialize the LIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        If either `key` or `item` is None, the method does nothing. If adding
        the item results in the cache size exceeding `MAX_ITEMS`, the most
        recently added item in the cache is discarded in accordance with the
        LIFO policy.

        Args:
            key: The key under which the item is stored.
            item: The item to be cached.

        Prints:
            A message indicating the discarded item when the cache limit
            is exceeded.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(discarded_key)
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
        return self.cache_data[key]
