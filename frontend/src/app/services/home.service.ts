import { Injectable } from '@angular/core';
import axios, { AxiosRequestConfig, AxiosRequestHeaders } from 'axios';

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

  private spotifyUrl = 'https://spotifly-manus.azurewebsites.net/api/getuserprofile?name=bleras';
  private data = null;

  constructor() { }

  public async getDatos():Promise<String> {
    try {
      const response = await axios.get(this.spotifyUrl, this.config);
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  
}
