import logging

import azure.functions as func
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
from spotipy.oauth2 import SpotifyClientCredentials

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    artist = req.params.get('artist')

    if not artist:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            artist = req_body.get('artist')
    
    if artist is None:
        return func.HttpResponse(
            "Please pass an 'artist' parameter on the query string",
            status_code=400
        )

    results = sp.search(q='artist:' + artist, type='artist')
    artists = results['artists']['items']

    artist_list = []
    for artist in artists:
        artist_dict = {'id': artist['id'], 'name': artist['name']}
        artist_list.append(artist_dict)

    if artist_list:
        return func.HttpResponse(json.dumps({'artists': artist_list}), status_code=200)
    else:
        return func.HttpResponse(json.dumps({'error': 'No artists found'}), status_code=404)
