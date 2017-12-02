
# Fibonacci Series
#  0, 1, 1, 2, 3, 5, 8, 13, ...

def sum_series(nth=1, sequence=[0,1]):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence[nth-1]






def sum_series_print(nth=1, sequence=[0, 1]):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
        print(sequence)
    return sequence[nth - 1]


def sum_series_tuple(nth=1, sequence=(0, 1)):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    sequence = list(sequence)
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
        print(sequence)
    return sequence[nth - 1]


def sum_series_none(nth=1, sequence=None):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    if sequence is None:
        sequence = [0, 1]
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
        print(sequence)
    return sequence[nth - 1]



d = {0: "this", 1: "that"}


def change_me(l=None):
    if l is None:
        l = []
    l.append(5)
    return l





def sum_series_tuple2(nth=1, sequence=(0, 1)):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    sequence = list(sequence)
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
        print(sequence)
    return sequence[nth - 1]





