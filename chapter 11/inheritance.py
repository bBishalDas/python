class anime:
    anime_name= "My dress-up darling"
    genre= "rom-com, cosplay"
    episodes=45
    def manga_adaptation(self):
        print(f"anime name: {self.anime_name}\ngenre: {self.genre}\nepisodes: {self.episodes}")

class manga():
    manga_name="My dress-up darling"
    volumes=56
    def anime_adaptation(self):
        print(f"manga name:{self.manga_name}\nvolumes: {self.volumes}")


class studio(anime,manga):
    studio_name="MAPPA"
    def studio_info(self):
        print(f"name of studio: {self.studio_name}")

a=anime()
b=studio()


b.manga_adaptation()
b.anime_adaptation()
b.studio_info()
