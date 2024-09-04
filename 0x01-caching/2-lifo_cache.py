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

    def put(self, key, item):
        """ Puts cache in the cache dictionary
        """
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]

            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                print("Discard: ", last_key)
                del self.cache_data[last_key]

            self.cache_data[key] = item

    def get(self, key):
        """ Gets the value of specific key
        """
        if not key or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
