class anime:
    anime_name= "My dress-up darling"
    genre= "rom-com, cosplay"
    episodes=45
    def manga_adaptation(self):
        print(f"anime name: {self.anime_name}\ngenre: {self.genre}\nepisodes: {self.episodes}")

class manga(anime):
    manga_name="My dress-up darling"
    volumes=56
    def anime_adaptation(self):
        print(f"\nmanga name:{self.manga_name}\nvolumes: {self.volumes}")


a= anime()
b=manga()

b.anime_adaptation
b.manga_adaptation