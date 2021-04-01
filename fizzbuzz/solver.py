from abc import ABC, abstractmethod


class Int2String(ABC):
    @abstractmethod
    def convert(self, number):
        "pass"


class Displayer(ABC):
    @abstractmethod
    def display(self, chaine):
        "pass"


class ProblemSolver(Int2String, Displayer):

    def __init__(self, converter, displayer):
        self.converter = converter
        self.displayer = displayer

    def convert(self, number):
        return self.converter.convert(number)

    def display(self, chaine):
        return self.displayer.display(chaine)

    def solve(self, n):
        i = 1
        while(i <= n):
            x = self.convert(i)[0]
            self.display(x)
            i += 1
