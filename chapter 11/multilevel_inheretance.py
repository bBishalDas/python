class x:
    def owner(self):
       print("1")
    a=5
class y(x):
    def manager(self):
       print("2")
    b=10
class z(y):
    def cleaner(self):
       print("3")
    c=15

e=x()
print(e.a)
f=y()
print(f.a,f.b)
g=z()
print(g.a,g.b,g.c)