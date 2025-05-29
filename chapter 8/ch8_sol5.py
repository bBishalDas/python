def pattern(n):
    if n==0:
        return
    for i in range(n):
     print("*"*n)
     n-=1

pattern(3)


def pattern(n):
     if n==0:
          return
     print("*"*n)
     pattern(n-1)

pattern(3)