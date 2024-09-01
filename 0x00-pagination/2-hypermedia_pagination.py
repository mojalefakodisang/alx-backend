#!/usr/bin/env python3
"""Module containing a Server class"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """Returns a tuple of size two with start index
            and end index
        """
        if page == 0 or page_size == 0:
            return ()
        res = [i * page_size for i in range(0, page + 1)]
        return (res[-2], res[-1])

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets paginated content
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing the following key-value pairs:
        """
        next_page = 0
        prev_page = 0

        if (page - 1) != 0 and self.get_page(page, page_size) is not None:
            prev_page = page - 1
        else:
            prev_page = None

        if ((page + 1) >= len(self.get_page(page, page_size)) and
                self.get_page(page + 1, page_size) is not None):
            next_page = page + 1
        else:
            next_page = None

        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
