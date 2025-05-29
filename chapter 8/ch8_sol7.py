def rem(l, word):
    n=[]
    for item in l:
        if item != word:
            n.append(item.replace(word, ""))
    return n

user_input=input("enter you sentence or set: ")

word=input("type the word you want to remove: ")

l=user_input.split()

print(" ".join(rem(l, word)))