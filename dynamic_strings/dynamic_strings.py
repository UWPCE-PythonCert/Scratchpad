#!/usr/bin/env python

"""
code for dynamic string formatting script
"""

# old style:
"My name is %s and I am %ift %iin tall" % ("Chris", 5, 10)

"My name is {:s} and I am {:d}ft {:d}in tall".format("Chris", 5, 10)

english = "My name is {:s} and I am {:d}ft {:d}in tall"
french = "Je m'appelle {:s} et je suis {:d}ft {:d}in tall"


def use_format_string(formatter):
    name = "Fred"
    height = (5, 10)
    return formatter.format(name, *height)


def display_items(seq):
    print("There are 3 items, and they are: {}, {}, {}".format(*seq))


def display_items(seq):
    l = len(seq)
    return ("There are {} items, and they are: " + ", ".join(["{}"] * l)).format(l, *seq)

