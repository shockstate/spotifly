import logging

import azure.functions as func
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    search_term = 'Aitana'

    results = sp.search(q='artist:' + search_term, type='artist')
    artists = results['artists']['items']

    artist_names = [artist['name'] for artist in artists]

    return func.HttpResponse(
        "\n".join(artist_names),
        status_code=200
    )
