class anime:
    name= "My dress-up darling"
    genre= "rom-com, cosplay"
    def manga_adaptation(self):
        print(f"genre: {self.genre},\nepisodes: {self.episodes}")

class manga(anime):
    name="My dress-up darling"
    def anime_adaptation(self):
        print(f"volumes: {self.volumes}")

