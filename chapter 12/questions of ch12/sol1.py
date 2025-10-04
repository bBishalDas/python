try:
    with open("1.txt", "r") as f:
        print(f"{f.read()}\n")
except Exception as e:
    print(f"{e}\n")

try:
    with open("2.txt", "r") as f:
        print(f"{f.read()}\n")
except Exception as e:
    print(f"{e}\n")

try:
    with open("3.txt", "r") as f:
        print(f"{f.read()}\n")
except Exception as e:
    print(f"{e}\n")

print("thank you!")