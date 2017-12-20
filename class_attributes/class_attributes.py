# class attributes tests.


class C:
    this = 5

    def __init__(self, that):
        self.that = that


class C:
    this = []

    def __init__(self, that):
        self.that = [that]



class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)





