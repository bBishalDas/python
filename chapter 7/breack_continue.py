for i in range(100):
    if i==35:
        break # exits the loop regardless of anything
    print(i)

l=[2,6,8,33,6,8,90000,6,3,44,7,97,4,6,8,5,3,45,7,8,6,43,55,77,444,334,678,433,68,443,567,443,566,343,678,234,789,444,78,578]
for i in l:
    if i==90000:
        continue # skips the iteration
    print(i)