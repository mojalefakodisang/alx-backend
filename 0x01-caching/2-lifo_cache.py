#!/usr/bin/env python3
""" Module containing a LIFO caching class
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class - Uses LIFO caching to discard caches
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Puts cache in the cache dictionary
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    last = self.order.pop()
                    print(f"DISCARD: {last}")
                    del self.cache_data[last]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Gets the value of specific key
        """
        return self.cache_data.get(key, None)
