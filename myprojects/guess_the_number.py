import random

input("to start the game press Enter.")

level=input("choose difficulty level (easy, medium, hard): ").lower()

if level =="easy":
    n = random.randint(0,20)
    print("number range:0-20")
    attempts=6

elif level=="medium":
    n = random.randint(0,40)
    print("number range:0-40")
    attempts=6

    if n%2==0:
        print("hint: your number is even.")
    else:
        print("hint: your number is odd.")

elif level=="hard":
    n = random.randint(0,80)
    print("number range:0-80")
    attempts=6

    if n%2==0:
        print("hint: your number is even.")
    else:
        print("hint: your number is odd.")

else:
    print("warning:the input you entered is invalid, please try again.")
    quit()

for computer in range(6):
    userch=int(input(f"attempts left: {attempts-computer} \nstart your gesses: "))
    if userch < n:
        print("go higher...")
    elif userch > n:
        print("go lower...")
    elif userch == n:
        print("you win.")
        break
else:
    print(f"better luck next time, you lose. your number was {n}.")