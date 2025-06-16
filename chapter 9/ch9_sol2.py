import random

def game9():
    entergame = input("To enter the game press enter or to quit type 'exit': ")

    if entergame.lower() == "exit":
        print("Thank you for playing.")
        return

    print("🎮 Welcome to the Number Guessing Game!")
    print("You have 5 tries to guess the number between 1 and 10.")

    target = random.randint(1, 3)
    score = 0

    for i in range(1, 6):  # 5 attempts
        try:
            user = int(input(f"\nAttempt {i} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user == target:
            print("🎉 Congratulations!! You guessed it right. You win!")
            score = 5 - (i - 1)  # More points for fewer attempts
            break
        else:
            print(f"❌ Wrong guess. You have {5 - i} tries left.")
    
    print(f"\nYour score: {score}")

    # High Score Logic
    try:
        with open("hyscore.txt", "r") as f:
            hiscore = f.read()
            hiscore = int(hiscore) if hiscore else 0
    except FileNotFoundError:
        hiscore = 0

    if score > hiscore:
        print("🏆 New High Score!")
        with open("hyscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High Score remains: {hiscore}")

game9()
