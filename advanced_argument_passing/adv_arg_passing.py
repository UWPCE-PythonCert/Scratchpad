#!/usr/bin/env python

"""
handy functions for demonstrating advanced arg passing
"""

def fun_pos(x, y, z):
    print(x, y, z)


def fun_kw(x=0, y=0, z=0):
    print(x, y, z)


def fun_comb(x, y, z=0, w=0):
    print(x, y, z, w)


def rect(x, y, w=10, h=10):
    print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))


position = (30, 40)
size = {'h': 10, 'w': 20}


def fun_arb(*args, **kwargs):
    print("the positional arguments are:", args)
    print("the keyword arguments are:", kwargs)


names = {"last": "Barker", "first": "Chris"}

# "My name is {first} {last}".format(**names)

# "My name is {first} {last}".format(last="Barker", first="Chris")

def fun_combo(x, y, *args, this=5, **kwargs):
    print(x, y, this)
    print(args)
    print(kwargs)


def fun_simple(x, y=0):
    print(x, y)


