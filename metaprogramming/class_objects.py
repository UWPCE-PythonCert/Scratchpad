class Simple():
    this = "a class attribute"

    def __init__(self):
        self.that = "an instance attribute"


# creating a class from scratch

atts = {'foo':'nice', 'bar':'sweet'}

type("CoolClass", (), atts)