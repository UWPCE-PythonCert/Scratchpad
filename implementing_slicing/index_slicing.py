#!/usr/bin/env python3

"""
examples / test code for __getindex__

Doesn't really do anything, but you can see what happens with different indexing.
"""

import operator

arr = [[i for i in range(r * 5, r * 5 + 5)] for r in range(4)]


def print_arr(arr):
    f_string = "[{}]".format(", ".join(["{:3}"] * len(arr[0])))
    print("[{}]".format("\n ".join([f_string.format(*row) for row in arr])))








class SimpleIndex:
    def __getitem__(self, index):
        print(index)















# class SimpleIndex:
#     def __getitem__(self, index):
#         print(index)
#         print(type(index))





class IndexTest:

    def __getitem__(self, index):
        # print("In getindex, indexes is:", index)
        if isinstance(index, slice):
            print("it's a single slice:", index)
        elif isinstance(index, tuple):
            print("it's a multi-dimensional slice:", index)
        else:
            try:
                # this converts arbitrary objects to an int.
                ind = operator.index(index)
                print("it's an index: ", ind)
            except TypeError:  # not a simple index
                raise
            print("It's a simple index")


if __name__ == "__main__":

    it = IndexTest()

    # print("calling with simple index")
    # it[4]

    # print("calling with single slice")
    # it[3:4]

    # print("calling with two slices")
    # it[3:4, 7:8]

    # print("calling with an invalid index")
    # it["this"]







