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
