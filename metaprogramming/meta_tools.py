"""
Sample code for tools for meta programing
"""


class Dummy:
    """A class with nothing in it"""
    pass


obj = Dummy()
setattr(obj, "name", "fred")

getattr(obj, "name")

att_name = 'this'
att_value = 'something'

setattr(obj, att_name, att_value)

getattr(obj, att_name)


