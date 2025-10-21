#!/usr/bin/env python3
"""This module contains a helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
