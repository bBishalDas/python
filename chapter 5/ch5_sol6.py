d={}

for i in range(4):
    name = input("enter your name: ")
    lang = input("enter your fav coding language: ")
    d[name]= lang

for index, name in enumerate(d, start=1):
    print(f"{index}.{name} likes {d[name]}")