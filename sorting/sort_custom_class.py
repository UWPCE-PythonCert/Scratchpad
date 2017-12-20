#!/usr/bin/env python



import random


class Donor:
    """
    Micro donor class to demonstrate issues with less than implementation
    """
    def __init__(self, name, donations):
        """
        Initialize with a name and list of donations
        """
        self.name = name
        self.donations = donations

    def __repr__(self):
        return "Donor({},{})".format(self.name, repr(self.donations))




    # def __lt__(self, other):
    #     return (self.name < other.name and
    #             self.donations < other.donations)

    # def __lt__(self, other):
    #     if self.name < other.name:
    #         return True
    #     elif self.name == other.name:
    #         return self.donations < other.donations
    #     else:
    #         return False

    # def __lt__(self, other):
    #     return (self.name, self.donations) < (other.name, other.donations)

    @staticmethod
    def sort_key(self):
        return (self.name, self.donations)







# Some examples:
a1 = Donor("Abe", [1])
a2 = Donor("Abe", [2])
a3 = Donor("Abe", [3])

b1 = Donor("Bob", [1])
b2 = Donor("Bob", [2])
b3 = Donor("Bob", [3])

c1 = Donor("Chuck", [1])
c2 = Donor("Chuck", [2])
c3 = Donor("Chuck", [3])


all_sorted = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
all_random = all_sorted[:]
random.shuffle(all_random)




def test_lt_1():
    """
    Abe should always be less than Bob
    """
    assert a2 < b1
    assert a2 < b2
    assert a2 < b3

    assert not b1 < a1
    assert not b2 < a1
    assert not b3 < a1



# def test_lt_2():
#     d1 = Donor("Abe", [2])
#     d2 = Donor("Bob", [1])
#     assert d1 < d2
#     assert not d2 < d1


class Donor2:
    """
    Micro donor class to demonstrate issues with less than implementation
    """

    def __init__(self, first_name, last_name, donations):
        """
        Initialize with a name and list of donations
        """
        self.first_name = first_name
        self.last_name = last_name
        self.donations = donations

    def __lt__(self, other):
        return ((self.last_name, self.first_name, self.donations) <
                (other.last_name, other.first_name, other.donations)
                )

    @staticmethod
    def sort_key(self):
        return (self.last_name, self.first_name, self.donations)

    def __repr__(self):
        return "Donor({} {}, {})".format(self.first_name,
                                         self.last_name,
                                         repr(self.donations))


# sample data
names = [("Chris", "Barker"),
         ("Fred", "Jones"),
         ("Bob", "Smith"),
         ("Alice", "Cooper"),
         ("David", "Bowie"),
         ("Bill", "Clinton"),
         ("Chuck", "Berry"),
         ("Elvis", "Presley"),
         ]

donor_list = [Donor2(*name, [random.random() * 1000]) for name in names]



