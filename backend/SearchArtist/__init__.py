import logging

import azure.functions as func
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

from models.artist import Artist

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    artist = req.params.get('artist')
    
    if artist is None:
        return func.HttpResponse(
            "Please pass an 'artist' parameter on the query string",
            status_code=400
        )

    results = sp.search(q='artist:' + artist, type='artist')
    artists = [Artist.from_dict(item) for item in results['artists']['items']]

    if artists:
        return func.HttpResponse(json.dumps({'artists': artists}, default=Artist.artist_serializer), status_code=200)
    else:
        return func.HttpResponse(json.dumps({'error': 'No artists found'}), status_code=404)
