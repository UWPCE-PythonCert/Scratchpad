#!/usr/bin/env python

"""
An example of putting simple tests in a __name__ == "__main__" block.
"""


# defining some (trivial) functions here
def fun(x, y):
    return x + y


def fun2(x, y):
    return x - y


if __name__ == "__main__":
    # this will only run if run as a script
    print("Running the tests")

    assert fun(3, 4) == 7

    assert fun2(3, 4) == -1

    print("the tests pass")

