#!/usr/bin/env python

import random


rand_list = list(range(10))
random.shuffle(rand_list)

long_list = [(random.randint(1, 1000), random.randint(1, 1000))
             for i in range(10000)]

a_tuple = tuple(rand_list)

a_dict = {"Barker": 45,
          "Jones": 32,
          "Ahmed": 14,
          "Hinkley": 32,
          }

names = [("Chris", "Barker"),
         ("Fred", "Jones"),
         ("Bob", "Smith"),
         ("Alice", "Cooper"),
         ("David", "Bowie"),
         ]


def last_name(item):
    return item[1]
