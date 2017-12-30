#!/usr/bin/env python

"""
sample code for adding up immutables in loops video
"""

import random

# Simple way to add up stuff:


list_of_numbers = [random.randint(0, 100) for i in range(20)]

list_of_strings = ["this ", "that, ", "the other"]


def add_up_seq(seq, start=0):
    total = start
    for item in seq:
        total += item
    return total






def make_really_big_string(n):
    s = ""
    for i in range(n):
        s += "a medium sized string"
    return s


def make_really_big_string_join(n):
    s_list = ["a medium sized string" for i in range(n)]
    return "".join(s_list)






