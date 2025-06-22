import random

def game():
    print("you're playing a game...")
    score= random.randint(1, 69)
    # fetch file-
    with open("hiscore_sol2.txt") as f:
        hiscore= f.read()
        if hiscore!="":
            hiscore= int(hiscore)
        else:
            hiscore=0
    print(f"your score: {score}")
    if score>hiscore or hiscore=="":
        #  write hiscore in the file-
        with open("hiscore_sol2.txt", "w") as f:
            f.write(str(score))
    
    
    return score


game()
    

