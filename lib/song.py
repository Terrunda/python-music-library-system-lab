class Song:
    
    #Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {} #Stores a genre as a key, with the value being the number of songs for the specific genre.
    artist_count = {} #Stores an artist as a key, with the value being the number of songs an artist has created



    @classmethod
    def add_song_to_count(cls):
        cls.count +=1
    
    @classmethod
    def add_to_genres(cls, new_genre):
        if new_genre in cls.genres:
            return
        else:
            cls.genres.append(new_genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            return
        else:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre): #if genre doesnt exist in genre_count, add the key and set it to 1.
        if cls.genre_count[genre] not in cls.genre_count:
            cls.genre_count.update({str(genre): 1 })
        else:
            cls.genre_count[genre] +=1
    
    @classmethod
    def add_to_artists_count(cls, artist):
        if cls.artist_count[artist] not in cls.artist_count: #if artist doesn't exist in artist_count, add the artist as the key and set it to 1.
            cls.artist_count.update({str(artist): 1})
        else:
            cls.artist_count[artist] +=1
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(self.genre)
        self.__class__.add_to_artists(self.artist)
        self.__class__.add_to_genre_count(self.genre)
        self.__class__.add_to_artists_count(self.artist)

    

