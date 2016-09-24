#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module tests too_many_kittens function."""

def too_many_kittens(kittens, litterboxes, catfood=None):
    """This function determines if there are too many kittens.

    Args:
        kittens(int):Number of kittens.
        litterboxes(int):Number of litterboxes.
        catfood(bool):Specifies whether there is catfood True(1) or not False(0).

    Returns:
        Bool: Answers whether or not we have too many kittens (True or False.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, 1)
        True

    """
    answer = (not (litterboxes >= kittens and catfood))
    return answer
