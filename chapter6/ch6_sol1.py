s=[]

for i in range(4):
    n=int(input(f"enter variable a{i+1}: "))
    s.append(n)
    
largest= max(s)

print("this is the largest input:", largest)

# can also make the program like this-

a=int(input("\n\nenter variable a: "))
b=int(input("enter variable b: "))
c=int(input("enter variable c: "))
d=int(input("enter variable d: "))

largest=max(a,b,c,d)

print("the largest input:", largest)

# for the sake of the chapter i will now use the conditional statment-

a=int(input("\n\nenter variable a: "))
b=int(input("enter variable b: "))
c=int(input("enter variable c: "))
d=int(input("enter variable d: "))

if a>b and a>c and a>d:
    print(f"a has the largest input: {int(a)}")
elif b>a and b>c and b>d:
    print(f"b has the largest input: {int(b)}")
elif c>a and c>b and c>d:
    print(f"c has the largest input: {int(c)}")
else:
    print(f"d has the largest input: {int(d)}")