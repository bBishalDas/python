with open("content1.txt", "r") as f:
    content1=f.read()

with open("content2.txt", "r") as f:
    content2=f.read()

if content1==content2:
    print("both the selected files have the same content.")
else:
    print("the selected files does not have the same content.")