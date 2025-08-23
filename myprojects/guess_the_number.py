import random

input("to start the game press Enter.")

level=input("choose difficulty level (easy, medium, hard): ").lower()

if level =="easy":
    n = random.randint(0,20)
    print("number range:0-20")

elif level=="medium":
    n = random.randint(0,40)
    print("number range:0-40")

elif level=="hard":
    n = random.randint(0,80)
    print("number range:0-80")

else:
    print("warning:the input you entered is invalid, please try again.")
    

for computer in range(6):
    userch=int(input("start your gesses: "))
    if userch < n:
        print("go higher...")
    elif userch > n:
        print("go lower...")
    elif userch == n:
        print("you win.")
        break
else:
    print(f"better luck next time, you lose. your number was {n}")