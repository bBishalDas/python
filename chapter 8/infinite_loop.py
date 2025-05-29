while True:
    x = int(input("x= "))
    y = int(input("y= "))
    r = input("enter 'add' to continue or 'end' to stop the program: ")

    if r.lower() == 'end':
        print("loop end")
        break
    else:
         print(x*y)