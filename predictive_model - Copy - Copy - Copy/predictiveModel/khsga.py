class A:
    def __init__(self):
        self.calc_i(456)

    def calc_i(self, i):
        self.i = 36 * i;


class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)

    def calc_i(self, i):
        self.i = 5 * i;


b = B()