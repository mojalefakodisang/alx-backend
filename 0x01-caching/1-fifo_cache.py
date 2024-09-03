#!/usr/bin/env python3
""" Module containing a FIFOCache class
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache uses the first-in first-out algorithm
    """

    def put(self, key, item):
        """ Put caches in the cache dictionary using FIFO
            algorithm
        """
        if key and item:
            self.cache_data[key] = item
            first_key = next(iter(self.cache_data))

            if len(list(self.cache_data.keys())) > BaseCaching.MAX_ITEMS:
                print(f'DISCARD: {first_key}')
                del self.cache_data[first_key]

    def get(self, key):
        """ Gets a cache by key from cache dictionary
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
