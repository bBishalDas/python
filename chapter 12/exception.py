# try: 
#     a=int(input("enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)

# print("enter a valid number")

# you can also specify or choose a error/exception type using try and except

    
try:
    a=int(input("enter divident: "))
    b=int(input("enter divisor: "))
    print(a/b)
except ZeroDivisionError as z: # this here shows the can't divid by zero error at the end of the not crashed program.
    print(z)

print("this was an error")