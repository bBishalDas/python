# this is far more efficient than the 1st solution as you don't have to repeat the same code 8 times.
s=set()

for i in range(8):
    n=input(f"{i+1} enter your number here: ")
    s.add(int(n))
print(s)