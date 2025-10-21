#!/usr/bin/python3
"""
This module provides a basic caching system implementation called `BasicCache`
which is derived from `BaseCaching`. The `BasicCache` class provides methods
to store key-value pairs in memory without any cache eviction policy, meaning
that the cache can grow indefinitely until it is explicitly cleared or the
program ends.

Classes:
    BasicCache - a basic cache that allows adding and retrieving items by key.

Usage Example:
    cache = BasicCache()
    cache.put("A", "Apple")
    print(cache.get("A"))  # Output: "Apple"
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    This class does not have any cache replacement policy.
    """
    def __init__(self):
        """Initialize the BasicCache instance."""
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: the key for the item
            item: the item to be cached
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: the key for the item

        Returns:
            The item if found, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
