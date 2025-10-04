try:
    a= int(input("enter a: "))
    b= int(input("enter b: "))
    print(f"a/b= {a/b}")
except ZeroDivisionError as z:
    print("infinite")

print("thank you.")
