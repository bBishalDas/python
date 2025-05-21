# checks if the username has more or less than 10 char in it.
username=input("enter your username here: ")

if len(username)<10:
    print("your username has less than 10 char")
else:
    print("your username has more or equal to 10 char")