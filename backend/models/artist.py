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
        return cls(id, name, popularity, followers, genres)
    
    def to_dict(self):
        return {'name': self.name, 'id': self.id}
    
    def artist_serializer(obj):
        if isinstance(obj, Artist):
            return obj.to_dict()
        raise TypeError(f'Object of type {type(obj)} is not JSON serializable')