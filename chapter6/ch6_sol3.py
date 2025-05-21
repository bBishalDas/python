
p1 = "click this"
p2 = "buy now"
p3 = "make a lot of mne"
p4 = "fast money"
p5 = "subscribe this"


message=input("enter comment: ")

if  p1 in message or p2 in message or p3 in message or p4 in message or p5 in message:
    print("this is a spam")
else:
    print("this is not a spam")