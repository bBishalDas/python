# # 1. integer
# a=3
# b=5
# # 2. floating point number
# c=33.6
# d=44.33
# # 3. booleans
# e=True
# # 4. none variable
# f=None
# # 5. strings
# g="bishal"

# # the same rules of c languade, to give names to variables will be applied in python
# # can't use symbols other than "_" on space b/t characters no number at the start of the name of the variable 

# a=8
# a-=2 if not (3==4) else 7
# print(a)

# n = 7
# n -= 1 if n % 2 == 0 else n + 1

# print(n)

n=8
n= n + 5 if 4==9 or 2>3 and 3<9 or 5==7 else n+7
t= type(n)
print(n)
print(t)

n=9
n= n + 7 if 4==9 or 2<3 and 3<9 or 5==7 else n+34
t= type(n)
print(n)
print(t)

n=8
n+= 5 or 4==9 or 2>3 and 3<9 or 5==7 and n+7
t= type(n)
print(n)
print(t)