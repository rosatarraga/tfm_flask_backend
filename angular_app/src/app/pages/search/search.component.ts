import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { tap } from 'rxjs';
import { DataService } from '../home/services/data.service';
import { Result } from './interfaces/result.interface';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  email: string;
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);
  results: Result[];
  displayedColumns: string[] = ['patientID', 'score', 'date'];



  constructor(
    private dataService: DataService,
  ) { }

  ngOnInit(): void {
  }

  getResults() {
    this.dataService.getResults(this.email)
    .pipe(
      tap((results:Result[]) => this.results=results)
    )
    .subscribe();
  }

}
