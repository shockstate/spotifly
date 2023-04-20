import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent  {

  public response: String = "";

  constructor(private homeService: HomeService) { }

  async createPlaylist(): Promise<void> {
    try {
      this.response = await this.homeService.makePlaylistRequest();
    } catch (error) {
      console.error(error);
    }
  }
  
}
