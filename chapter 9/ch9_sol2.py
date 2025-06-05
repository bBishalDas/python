import random    


def game9():
    entergame=input("To enter the game press enter or to quit type 'exit.'")
    for i in range(1, 11):
     if entergame=="exit":
        print("thank you for playing.")
        break
     
     if entergame=="yes":

        print("welcome to the number guessing game\nyou have 5 turns to guess the number from 1-10")
        
     user=int(input("\nEnter your guess: "))
     computer= random.randint(1, 10)
     score=0
     if user==computer:
       print("\ncongratulations!! you guessed correct. you win")
       score+=1
     elif user!=computer:
       print(f"ohhh! you guessed wrong. try again. you have {10-i} turns left.")
    
    with open("hyscore.txt") as f:
       hiscore= f.read()
       if hiscore!="":
          hiscore=int(score)
       else:
          hiscore=0
       
       if score>hiscore:
          with open("hyscore.txt"):
             f.write(str(score))

     

game9()


    

        


