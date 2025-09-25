# finally block will get exicuted no matter what

# def prpgram():
#     try:
#         a=int(input("enter number: "))
#         print(a)
#         return
#     except ValueError as e:
#         print(e)
#         return
#     finally:
#         print("i work no matter what.")

# prpgram()


def prpgram():
    try:
        a=int(input("enter number: "))
        print(a)
        return
    except ValueError as e:
        print(e)
        return
    
        print("this won't work if the program is returned work no matter what.")

prpgram()