#!/usr/bin/env python3
"""Module that contains a class BasicCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache
    """

    def put(self, key, item):
        """ Puts caches on cache dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets caches from cache dictionary
        """
        if key not in self.cache_data.keys() or key is None:
            return None

        return self.cache_data[key]
