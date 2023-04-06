import logging

import azure.functions as func
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scope = "user-library-read playlist-modify-public"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()
    tracks = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        tracks.append(track["id"])
    user = sp.current_user()
        
    create_playlist = sp.user_playlist_create(user['id'], "Test playlist", public=True, collaborative=False, description='My api playlist')
    sp.user_playlist_add_tracks(user['id'], create_playlist['id'], tracks, position=None)

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    return func.HttpResponse(
            "Created",
            status_code=201
    )
