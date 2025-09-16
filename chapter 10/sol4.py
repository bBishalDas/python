import math

class calculator:
    def __init__(self, n):
        self.n=n

    def square(self):
        print(f" The square of {self.n} is: {self.n*self.n}")

    def squareroot(self):
        print(f" The squareroot of {self.n} is: {math.sqrt(self.n)}")

    def cube(self):
        print(f" The cube of {self.n} is: {self.n*self.n*self.n}")

    @staticmethod
    def hello():
        print("hello there!!")   



n=int(input("enter a number: "))
a=calculator(n)
a.hello()
a.square()
a.squareroot()
a.cube()
        