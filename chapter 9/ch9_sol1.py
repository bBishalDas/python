with open("forsol1.txt") as f:
    read=f.read()
    # print(read)
if "noice" in read:
    print("this file content has the word 'noice'.")
else:
    print("this file doesn't have the required word.")