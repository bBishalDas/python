with open("log.txt", "r") as f:
    lines=f.readlines()

lineno=1

for line in lines:
    if "python" in line:
        print(f"the word 'python' is present in this file on the line number: {lineno}")
        break
    lineno+=1
else:
    print("this word doesn't exsit in this file.")