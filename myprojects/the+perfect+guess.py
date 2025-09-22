from random import randint

print("you have six turns, the game starts now!!")

level=int(input("Choose your leven you want to play:\n1. 🥱EASY\n2. 😥HARD\n3. 💀IMPOSSIBLE\n Enter assigned number to select the level:"))

if level==1:
    lvl= "🥱EASY"
    rang="0-20"
    computer= randint(0,20)
    turns=6
elif level==2:
    lvl= "😥HARD"
    rang="0-50"
    computer= randint(0,50)
    turns=7
elif level==3:
    lvl= "💀IMPOSSIBLE"
    rang="0-100"
    computer= randint(0,100)
    turns=8

print(f"your level: {lvl}, range: {rang}, and number of turns: {turns}")

for turns in range(turns):
     user=int(input("👉 enter your guess her: "))
     if computer < user:
         print(f"go lower👇👇, turns used {turns}")
     elif user < computer:
         print(f"go higher☝☝, turns used {turns}")
     elif computer == user:
         print("🏆you win🏆")
         break
     else:
       print("🔴ERROR: warning your entry is not a number, please enter a number and try again.")

else:
    print(f"😩😩looks like you ran out of turns, better luck next time, your number was {computer}.")
