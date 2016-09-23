#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Combines several variables into a string.

    Args:
        wink (str): Str to be repeated numwink times.
        numwink (int, optional): Int by which wink will be repeated. Defautl: 2.

    Returns:
        str: All arguments concatenated as specified.

    Examples:

        >>> know_what_i_mean('zaul')
        'Know what I mean? zaulzaul, nudge nudge'

        >>> know_what_i_mean('5')
        'Know what I mean? 55, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
