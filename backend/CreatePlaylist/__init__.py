import logging
import random
from typing import List

import azure.functions as func

from services.SpotipyClient import SpotipyClient

spotipy_client: SpotipyClient = None

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    global spotipy_client
    spotipy_client = SpotipyClient(scope='user-library-read playlist-modify-public')

    req_body = req.get_json()
    artists_ids = req_body.get('artistsIds')
    playlist_name = req_body.get('playlistName')

    songs_ids = getSongsIdsByArtists(artists_ids)
    random.shuffle(songs_ids)

    spotipy_client.createUserPlaylist(playlist_name, songs_ids)

    return func.HttpResponse(
            "Created",
            status_code=201
    )

def getSongsIdsByArtists(artists: List[str]) -> List[str]:
    songs = []
    for _, item in enumerate(artists):
        top_songs = getTopSongsIdsByArtist(item)
        songs.append(top_songs)
    return top_songs

def getTopSongsIdsByArtist(artist_id: str) -> List[str]:
    global spotipy_client
    return spotipy_client.getSongsByArtist(artist_id)
