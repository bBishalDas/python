
def word_remover():
    output_=[]
    user_input=input("type your text here: ").lower().split()
    words=input("enter the word to be removed: ")
    for word in user_input:
        if word in words:
            word=words.remove()
            output_=user_input.append(output_)
    return" ".join(user_input)




