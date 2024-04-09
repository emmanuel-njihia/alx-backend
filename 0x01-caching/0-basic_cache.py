#!/usr/bin/env python3
"""caching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Reps an object that allows storing and
    retrieving items.
    """
    def put(self, key, item):
        """addsitem to cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
