try:     
    a=int(input("enter a number: "))
     
    print(a)
except ValueError as e:
    print(e)

else:
    print("i am inside a")

# a=int(input("enter a number: "))
# print(a)