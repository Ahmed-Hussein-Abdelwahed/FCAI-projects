class Song:
    """Class song which represent the song

    Attributes:
        name (str): Song name
        duration (float): Song time length
        artist (str): Song artist
        distributor (str): distribution organization name
        """

    def __init__(self, name, duration, artist, distributor):
        """Song init function

        Args:
            name (str): song name
            duration (float): song duration"""
        self.name = name
        self.duration = duration
        self.artist = artist
        self.distributor = distributor

    def show_info(self):
        print(f"Name:{self.name}\nLength:{self.duration}\nArtist:{self.artist}\nDistributor:{self.distributor}")


ob = Song('Turn down for what', 4.5, 'Unknown', 'Anghami')
ob.show_info()


