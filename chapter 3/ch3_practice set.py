# q1. print goodafter noon "name", the name should be user entered

name= input("enter your name here: ")

print(f"good afternoon {name}")
#  q2. write a program to fill in a letter tamplate

name1= input("enter a name: ")
emotion= input("enter an emotion: ")
action=input("enter any action: ")
twist= input("enter an twinty plot: ")
letter= '''Dear <|name|>
i really really <|emotion|>
please <|action|> and send
<|twist|>'''

print(letter.replace("<|name|>", name1).replace("<|emotion|>", emotion).replace("<|action|>", action).replace("<|twist|>", twist))
