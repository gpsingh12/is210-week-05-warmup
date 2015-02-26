#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Function takes two arguments

       Args:
           wink(str): Takes no default value.
           numwink(int): Takes default value of 2.
           winks(str): Arg is assigned vallues using mathematical computations.
           restr(mixed): return the value corresponding to arg winks and nudges.

       Return(str):
               returns a string value assigned to retsr.

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
