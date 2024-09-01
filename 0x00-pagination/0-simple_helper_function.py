#!/usr/bin/env python3
"""Module that contains a simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two with start index
        and end index
    """
    if page == 0 or page_size == 0:
        return ()
    res = [i * page_size for i in range(0, page + 1)]
    return (res[-2], res[-1])
