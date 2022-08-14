from numpy.random import randint

class influenceDetail(object):
    def __init__(self, name, score):
        self.name = name
        if (self.name == "Wheel Speed") or (self.name == "Current Speed"):
            self.score = 10
        else:
            self.score = randint(0,70)

    def to_dict(self):
      return {"name": self.name, "score": self.score}