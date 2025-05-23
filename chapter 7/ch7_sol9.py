'''
n=3
***
* *
***

n=4

****
*  *
*  *
****

n=5

*****
*   *
*   *
*   *
*****
'''


n=int(input("enter number: "))
print("*"*n)
for i in range(1, n-1):
     k=" "*(n-2)
     print(f"*{k}*")
print("*"*n)

for row in range(n):
     for col in range(n):
          if row==0 or row==n-1 or col==0 or col==n-1:
               print("*", end="")
          else:
               print(" ", end="")
     print("")

for i in range(1, n+1):
     if i==1 or i==n:
          print("*"*n, end="")
     else:
          print("*", end="")
          print(" "*(n-2), end="")
          print("*", end="")
     print("")