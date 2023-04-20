import { Component } from '@angular/core';
import { HomeService } from '../../services/home.service';
import { Subject } from 'rxjs';
import { debounceTime, switchMap } from 'rxjs/operators';
import { Subscription } from 'rxjs';

interface Artist {
  id: number;
  name: string;
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
  

  selectArtist(artist: Artist) {
    this.selectedArtists.push(artist);
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
