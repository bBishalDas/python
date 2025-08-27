import random

CHOICES = ("rock", "paper", "scissors")
IDX = {n:i for i,n in enumerate(CHOICES)}
score = {"you": 0, "cpu": 0}

while max(score.values()) < 3:
    try:
        p = IDX[input("rock/paper/scissors: ").strip().lower()]
    except KeyError:
        print("✖ invalid choice\n"); continue
    c = random.randrange(3)
    outcome = (p - c) % 3
    print(f"cpu -> {CHOICES[c]}")
    if outcome == 0: print("= draw\n")
    elif outcome == 1: score["you"] += 1; print("+ you win this round\n")
    else: score["cpu"] += 1; print("- cpu wins this round\n")

print(f"final: you {score['you']} – {score['cpu']} cpu. {'You win!' if score['you']>score['cpu'] else 'CPU wins!'}")
