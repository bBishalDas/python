# create a code to give the sum of two numbers
a= int(input("enter num1: "))
b= int(input("enter num2: "))

print("sum of num1 + num2= ", a+b)

# print the remainder of two numbers
c= int(input("enter num3: "))
d= int(input("enter num4: "))

print("remainder of num1 and num2= ", c%d)

# print the data type of the data entered by input
t= type(input("enter any data type: "))

print("the entered data type is", t)

# shows which one of the entered numbers is greater
e= int (input(" enter the number 1: "))
f= int (input(" enter the number 2: "))

print("number 1 > number 2") if e>f else print(" number 2 > number 1")


# g= float(input("enter no.1: "))
# h= float(input("enter no.2: "))
# print("avarage of the 2 numbers is:", (g+h)/2)

i=float(input("enter any number: "))
n=float(input("enter power: "))
if n==0:
    print(" result is 1")
else:
    print("the square of the number is:", i**n)