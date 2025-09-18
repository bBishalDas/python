class define:
    t=12
    @classmethod # this allows for the self.t value to only be the set value inside the class
    def time(cls):
        print(f"this is the time {cls.t}")

a= define()

a.t=45 # 
a.time()
