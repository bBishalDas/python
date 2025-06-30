class best_player:
    rank= 'master'
    totalhours= "9999.hs"
    mvps= 986


    def __init__(self, name, rank): # fuctions starting with "__" are called dunder method which is automaticlly called 
                        # __init__ is called when is object is created
        self.name=name
        self.rank=rank
        print("i am creating a name")    


    def get_info(self):
        print(f"player name: {self.name} rank: {self.rank}, total hours played: {self.totalhours}, and has over {self.mvps} MVPs in total. True Legend")


unknown= best_player('bish', 342)
print(f'name: {unknown.name}')
unknown.get_info()