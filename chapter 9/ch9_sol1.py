# with open("forsol1.txt") as f:
#     read=f.read()
#     # print(read)
# if "noice" in read:
#     print("this file content has the word 'noice'.")
# else:
#     print("this file doesn't have the required word.")

with open("forsol1.txt") as f:
    read=f.read()
    print(read)
    word=input("enter the word you want to find: ")
if word in read:
    print(f"the word '{word}' is there in this file.")
else:
    print("word doesn't exist in this file.")

