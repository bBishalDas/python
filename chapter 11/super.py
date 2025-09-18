class employee:
    def __init__(self):
        print("employee section.")
    a=1

class manager(employee):
    def __init__(self):
        super().__init__()
        print("manager section.")
    b=2

class CEO(manager):
    def __init__(self):
        super().__init__()
        print("CEO ection.")
    c=3

# a=employee()
# print(a.a)


# b=manager()
# print(b.a)


c=CEO()
print(c.c)