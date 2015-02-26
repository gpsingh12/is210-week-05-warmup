#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Takes 3 arguments and return bool value True if second argument
       is greater than other two.

       Args:
            kittens(int):     Argument provides no. of kittens.
            litterboxes(int): Argumentlists the no. of available litterboxes.
            catfood(bool):    Boolean represting whether catfood exists or not.

       Returns:
               returns boolean value of True of acomparison operator if
               litterboxes are greater than or equal to kittens and catfood.
    """
    return not(litterboxes >= kittens and catfood)
