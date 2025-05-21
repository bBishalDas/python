# whit input function and for loop
nam= input("enter names here:").split()

for name in nam:
    if name.lower().startswith("s"):
     print(f"Hello, {name}")

# with input function and list
nam = input("enter names here with commas: ")
names = []

for name in nam.split(","):
    names.append(name.strip())

for name in names:
    if name.lower().startswith("s"):
       print(f"hello, {name}")


# with no input function
l=["ritu", "bishal", "shubha", "sita"]

for name in l:
    if name.startswith("s"):
        print(f"hello, {name}")
    