#!/usr/bin/env python3
"""
Module for task 09
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the length of a list of sequences
    """
    return [(i, len(i)) for i in lst]
