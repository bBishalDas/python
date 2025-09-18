class number:

    def __init__(self, n):
        self.n=n
    def __add__(self, num):
        return self.n + num.n

a=number(1)
b=number(2)

print(a+b)