class best_player:
    rank= 'master'
    totalhours= "9999.hs"
    mvps= 986
        
    def get_info(self):
        print(f"rank: {self.rank}, total hours played: {self.totalhours}, and has over {self.mvps} MVPs in total. True Legend")

# want a atrribute which don't need an object to represent itself? use "@sataticmathod"-
    @staticmethod
    def hi():
        print("hello!!")


unknown= best_player()
unknown.name="unknown"
print(f'name: {unknown.name}')
unknown.get_info()
# one more way to activate function get_info-

best_player.get_info(unknown)

unknown.hi()