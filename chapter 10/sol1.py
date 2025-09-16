class programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin


name=input("enter name: ")
pin=input("enter pin code: ")

p=programmer(name, 120000, pin)

print(f" name: {p.name},\n salary: {p.salary},\n pin code: {p.pin},\n company: {p.company}")