from random import randint

class train:
    
    def __init__(self, train_no):
        self.train_no=train_no
    
    def getbooking(self,fro,to):
        print(f"your ticket has been booked of {fro} to {to}, train no. {self.train_no}")

    def status(self):
        print(f"train no. {self.train_no} is running on time.")
    
    def fare(self):
        print(f"the fare of the train no. {self.train_no} is {randint(777,999)}/- and seat no. {randint(1,500)}")


about_train=train(1233)
about_train.getbooking("jaipur", "pune")
about_train.status()
about_train.fare()