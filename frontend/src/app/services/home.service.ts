import { Injectable } from '@angular/core';
import axios, { AxiosRequestConfig, AxiosRequestHeaders } from 'axios';



interface PlaylistRequest {
  artistsIds: Array<String>;
  playlistName: String;
}

@Injectable({
  providedIn: 'root'
})

export class HomeService {

  private config : AxiosRequestConfig = {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  };

  private createPlaylistUrl = 'http://localhost:7071/api/CreatePlaylist';
  private searchArtistUrl = 'http://localhost:7071/api/SearchArtist';

  constructor() { }

  public async createPlaylistRequest(playlistRequest:PlaylistRequest):Promise<String> {
    try {
      const response = await axios.post(this.createPlaylistUrl, playlistRequest, this.config);
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  public async getArtists(artist: string): Promise<any> {
    try {
      const response = await axios.get(`${this.searchArtistUrl}?artist=${artist}`, this.config);
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
  

  
}
