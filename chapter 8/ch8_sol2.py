def fahrenheit_to_celsius(f):
     return 5*(f-32)/9

while True:
    r=input("\nto proceed with the convertion type 'yes'\nor 'end' to exit the program: ")
    if r.lower() == 'end':
         print("thank you, the program ends here.")
         break
    elif r=='yes':
        user=float(input("enter the tempreture: "))
        c=fahrenheit_to_celsius(user)
        print(f"{round(c, 2)}°c")
    else:
        print("\nERROR: this is not a valid entry. please type a valid entry.")