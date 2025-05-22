n=int(input("type in your number: "))

for i in range(2, n):
  if n%i==0:
     print(f"{n} is not prime number.")
     break
else:
   print(f"{n} is a prime number.")