#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


def defaults(my_required, my_optional=True):
    """ Consists of two arguments, one has a default value and return bool.

        Args:
            my_required(Bool): Argument has no default value.
            my_optional(Bool): Argument has a default value True.

        Returns:
            Bool: Function returns bool values when passed.
    """

    return my_optional is my_required
