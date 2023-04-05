import logging

import azure.functions as func
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scope = "user-library-read"
    logging.info(os.environ["SPOTIPY_CLIENT_ID"])
    logging.info("test")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    return func.HttpResponse(
            "Created",
            status_code=201
    )
