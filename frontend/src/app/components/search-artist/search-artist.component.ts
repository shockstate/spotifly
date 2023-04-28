import { Component } from '@angular/core';
import { HomeService } from '../../services/home.service';
import { Subject } from 'rxjs';
import { debounceTime, switchMap } from 'rxjs/operators';
import { Subscription } from 'rxjs';

interface Artist {
  id: String;
  name: String;
}

interface PlaylistRequest {
  artists: Array<String>;
  playlistName: String;
}

@Component({
  selector: 'app-search-artist',
  templateUrl: './search-artist.component.html',
  styleUrls: ['./search-artist.component.scss']
})
export class SearchArtistComponent {
  public artistInput = '';
  public artists: Artist[] = [];
  public selectedArtists: Artist[] = [];
  public response: String = "";
  public showModal : Boolean = false;
  public playlistName : String = '';

  private searchSubject = new Subject<string>();
  private subscription: Subscription = new Subscription();

  constructor(private homeService: HomeService) {
    this.setupArtistSearch();
  }

  setupArtistSearch() {
    this.subscription = this.searchSubject
      .pipe(
        debounceTime(500),
        switchMap((searchText) => this.homeService.getArtists(searchText))
      )
      .subscribe({
        next: (data) => {
          this.artists = data.artists;
        },
        error: (error) => {
          console.error(error);
        }
      });
  }

  onInputChange() {
    const inputText = this.artistInput.trim();
    if (inputText.length > 0) {
      this.searchSubject.next(inputText);
    } else {
      this.artists = [];
    }
  }

  async sendPlaylist(): Promise<void> {
    const artistIds = this.selectedArtists.map(artist => artist.id);

    const playlistRequest: PlaylistRequest = {
      artists: artistIds,
      playlistName: this.playlistName
    }

    try {
      this.response = await this.homeService.createPlaylistRequest(playlistRequest);
    } catch (error) {
      console.error(error);
    }
  }
  
  selectArtist(artist: Artist) {
    this.selectedArtists.push(artist);
  }

  savePlaylist() {
    this.showModal = false;
    this.playlistName = '';
  }

  openModal() {
    this.showModal = true;
  }

  removeArtist(artist: Artist) {
    const index = this.selectedArtists.indexOf(artist);
    if (index > -1) {
      this.selectedArtists.splice(index, 1);
    }
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
