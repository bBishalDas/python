a=int(input("enter number1: "))
b=int(input("enter number2: "))

if (b==0):
    raise ZeroDivisionError ("hey this program is not meant to divid with zero.")
# raising an error crashes a program and gives a costum error, helping the developer to know thier mistake.
else:
    print(f"your division is: {a/b}")