#!/usr/bin/python3
"""
This module provides a caching system implementation, `FIFOCache`, which
follows a First-In-First-Out (FIFO) caching policy. The class inherits from
`BaseCaching` and has a fixed cache size defined by `MAX_ITEMS`. When the
cache exceeds this limit, the oldest item (the first item added) is
automatically discarded.

Classes:
    FIFOCache -- a cache system that evicts items in a FIFO order when reaching
                 the maximum cache size.

Usage Example:
    cache = FIFOCache()
    cache.put("A", "Apple")
    cache.put("B", "Banana")
    print(cache.get("A"))  # Output: "Apple"
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class

    This class implements a cache system with a First-In-First-Out (FIFO)
    eviction policy. When the number of items in the cache exceeds `MAX_ITEMS`,
    the oldest item added to the cache is removed to make space for the
    new item.

    Methods:
        put(key, item) -- Adds an item to the cache. If the cache exceeds the
                          limit, the oldest item is removed.
        get(key) -- Retrieves an item from the cache by key.
    """
    def __init__(self):
        """
        Initialize the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        If either `key` or `item` is None, the method does nothing. If adding
        the item results in the cache size exceeding `MAX_ITEMS`, the oldest
        item in the cache is discarded in accordance with the FIFO policy.

        Args:
            key: The key under which the item is stored.
            item: The item to be cached.

        Prints:
            A message indicating the discarded item when the cache limit is
            exceeded.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = next(iter(self.cache_data.items()))
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
