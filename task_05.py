#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Boolean function."""

def defaults(my_required, my_optional=True):
    """Function compares parameters by logical operator is.

    Args:
        my_required(bool):Is either True(1) or False(0).
        my_optional(bool, optional):Is either True(1) or False(0). Default:True.

    Returns:
        Bool: True or False.

    Examples:
    
        >>> defaults(True, False)
        False

        >>> defaults(True, 0)
        False
    
    """
    MYOP = my_optional is my_required
    return MYOP

    print MYOP
