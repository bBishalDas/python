import random

wapons=("rock", "paper", "scissors")

print("rock")
print("paper")
print("scissors")

def battle():
    user=input("enter your choose of weapon: ")
    computer=random.choice(wapons)
    
    ccount=0
    ucount=0

    if computer==user:
        print("this was a tie.")
    elif ((computer == "rock") and (user == "scissors")) or ((computer=="paper") and (user=="rock")) or ((computer=="scissors") and (user=="paper")):
        print("computer scores a point!!")
        ccount+=1
    else:
        print("you scored a point!!!")
        ucount+=1

    if user=="exist":
        if ccount<ucount:
         print(f"you won!!! your score {ucount}. thank you for playing.")
         quit()
        else:
            print(f"computer win, its score {ccount} better luck next time.")
            quit()



    return battle()

battle()