import random

def game():
    score=random.randint(1, 70)
    with open("hyscore.txt") as hyscore:
        hyscore= hyscore.read()
        if hyscore!="":
            hyscore=int(hyscore)
        else:
            hyscore=0

    print(f"your score: {score}")
    if score>hyscore:
        with open ("hyscore.txt", "w") as f:
            f.write(str(score))
    return score

game()


