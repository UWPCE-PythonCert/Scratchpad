#!/usr/bin/env python

"""
Example code for the properties video
"""

class JavaStyle:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def __repr__(self):
        return "JavaStyle({})".format(self.get_x())





class PythonStyle:

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "PythonStyle({})".format(self.x)










class PythonStyle:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        if val < 0:
            raise ValueError("x can't be less than zero")
        self._x = val

    @property
    def y(self):
        return 2*self.x
    @y.setter
    def y(self, val):
        self.x = val / 2






    def __repr__(self):
        return "PythonStyle({})".format(self.x)


# class PythonStyle:

#     def __init__(self, x):
#         self.x = x

#     def y(self):
#         return self.x * 2

#     def __repr__(self):
#         return "PythonStyle({})".format(self.x)

# class PythonStyle:

#     def __init__(self, x):
#         self.x = x

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, val):
#         if val < 0.0:
#             raise ValueError("x can not be less than zero")
#         else:
#             self._x = val

#     @property
#     def y(self):
#         return self.x * 2

#     @y.setter
#     def y(self, val):
#         self.x = val / 2

#     def __repr__(self):
#         return "PythonStyle({})".format(self.x)

