#!/usr/bin/python3
"""finding the peak"""


def find_peak(list_of_integers):
    """find the peak """
    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])
    else:
        return None
