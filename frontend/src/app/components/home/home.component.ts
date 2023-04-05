import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  datos: any;

  constructor(private homeService: HomeService) { }

  async ngOnInit(): Promise<void> {
    try {
      this.datos = await this.homeService.getDatos();
    } catch (error) {
      console.error(error);
    }
  }
}
