class Artist:
    def __init__(self, id, name, popularity, followers, genres):
        self.name = name
        self.id = id
        self.popularity = popularity
        self.followers = followers
        self.genres = genres

    @classmethod
    def from_dict(cls, artist_dict):
        name = artist_dict['name']
        id = artist_dict['id']
        popularity = artist_dict['popularity']
        followers = artist_dict['followers']['total']
        genres = artist_dict['genres']
        return cls(name, id, popularity, followers, genres)