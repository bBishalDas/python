import random
'''
gun 0 beats snake 1,
water -1 beats gun 0,
snake 1 beats water -1
'''

inputstr={'snake':1, 'water':-1, 'gun':0}
showoutpt={1:'🐍snake', -1:'💧water', 0:'🔫gun'}

user_score = 0
computer_score = 0
draws = 0

def print_scoreboard():
    print("\n" + "="*30)
    print(f"{'SCOREBOARD':^30}")
    print("="*30)
    print(f"{'You':<10}: {user_score}")
    print(f"{'Computer':<10}: {computer_score}")
    print(f"{'Draws':<10}: {draws}")
    print("="*30)

n=int(input("enter the number of turns you wanna play for: "))    

for _ in range(n+1):
    
    userinput= input("ENTER YOUR CHOICE (or type 'exit' to quit.): ").lower()
    if userinput=="exit":
        print("thank you for playing😊")
        break
    if userinput not in inputstr:
        print("Invalid input. Please choose 'snake', 'water', or 'gun'.")
        continue

    computer = random.choice([1,-1,0])
    user=inputstr[userinput]

    print(f"your choice {showoutpt[user]}\ncomputer's choice {showoutpt[computer]}")

    
    if (computer==user):
        print("its a draw😑")
        draws += 1
    
    elif(computer==-1 and user==1 or computer==0 and user==-1 or computer==1 and user==0):
        print("you win.😒")
        user_score += 1

    elif(computer==1 and user==-1 or computer==-1 and user==0 or computer==0 and user==1):
        print("i win HAHA.😚")
        computer_score += 1




print_scoreboard()

if user_score>computer_score:
        print("You win. I know you cheated!!😣")
elif user_score<computer_score:
        print("HAHA I win, I am the best!! 🥳")
else:
     print("its a draw.")