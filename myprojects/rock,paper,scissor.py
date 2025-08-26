import random

game_wapons={
    1: "rock",
    2: "paper",
    3: "scissors"
}


game_of=input(f"choose game of: a) 6 points, b) 11 points or c) infinite: ")

ucount=0
ccount=0
# conditional statments for wins and losses

# loops to keep the game going
if game_of=="a":
   for g in range(7):
     user=input(f"\nrock,\npaper,\nscissors\nchoose your weapon: ")
     computer=random.choice(list(game_wapons.values()))

     if user not in game_wapons.values() and user!="exit":
         print("Error: the your input is invalid. please enter correct weapons.")
         continue

     elif computer==user:
       print(f"computer:{computer}")
       print("\nits a tie, try again.")

     elif ((computer=="rock")and(user=="scissors")) or ((computer=="scissors")and(user=="paper")) or ((computer=="paper")and(user=="rock")):
        print(f"computer: {computer}")
        print("\ncomputer scores!!")
        ccount+=1

     elif ((user=="rock")and(computer=="scissors")) or ((user=="scissors")and(computer=="paper")) or ((user=="paper")and(computer=="rock")):
        print("\nyou scored!!")
        ucount+=1


elif game_of=="b":
    for g in range(12):
      user=input(f"\nrock\npaper\nscissors\nchoose your weapon: ")
      computer=random.choice(list(game_wapons.values()))           
      
      if user not in game_wapons.values() and user!="exit":
         print("Error: the your input is invalid. please enter correct weapons.")
         continue
        
      elif computer==user:
       print(f"computer:{computer}")
       print("\nits a tie, try again.")

      elif ((computer=="rock")and(user=="scissors")) or ((computer=="scissors")and(user=="paper")) or ((computer=="paper")and(user=="rock")):
        print(f"computer: {computer}")
        print("\ncomputer scores!!")
        ccount+=1

      elif ((user=="rock")and(computer=="scissors")) or ((user=="scissors")and(computer=="paper")) or ((user=="paper")and(computer=="rock")):
        print("\nyou scored!!")
        ucount+=1


elif game_of=="c":
    while True:
        print("nice choise, type 'exit' when you want to stop.")
        
        user=input(f"\nrock,\npaper,\nscissors\nchoose your weapon: ")
        computer=random.choice(list(game_wapons.values()))

        if user not in game_wapons.values() and user!="exit":
          print("Error: the your input is invalid. please enter correct weapons.")
          continue

        elif user=="exit":
            print("GG, lets play again sometime.")
            break
        else:
                    
         if computer==user:
          print(f"computer:{computer}")
          print("\nits a tie, try again.")

         elif ((computer=="rock")and(user=="scissors")) or ((computer=="scissors")and(user=="paper")) or ((computer=="paper")and(user=="rock")):
           print(f"computer: {computer}")
           print("\ncomputer scores!!")
           ccount+=1

         elif ((user=="rock")and(computer=="scissors")) or ((user=="scissors")and(computer=="paper")) or ((user=="paper")and(computer=="rock")):
           print("\nyou scored!!")
           ucount+=1

# counters to keep score

uscore=print(f"\nyour score: {ucount}")
comscore=print(f"computer score: {ccount}")

if ucount>ccount:
  print("\ncongratulations!! you win!!")
else:
  print("\nbetter luck next time. computer wins!!")
# error department (meaning if the user's input is not valid)