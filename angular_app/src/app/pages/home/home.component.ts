import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from 'src/app/pages/home/services/data.service';
import { FileValidator } from 'ngx-material-file-input';
import { tap } from 'rxjs';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';

class ImageSnippet {
  constructor(public src: string, public file: File) { }
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  email: string;
  idPat: string;
  view: string;
  file: File;
  url: any;
  selectedFile: ImageSnippet;
  maxSize: number = 100000000;
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);
  idPatFormControl = new FormControl('', Validators.required);
  mamoFormControl = new FormControl('', Validators.required);
  imageSizeControl = new FormControl(null, FileValidator.maxContentSize(this.maxSize));

  mamos: string[] = ['L-MLO', 'R-MLO','L-CC', 'R-CC'];
    

  constructor(
    private dataService: DataService,
    private router: Router,
    public dialog: MatDialog
  ) { }

  ngOnInit(): void {

  }


  processFile() {
    
    // this.dataService.uploadImage(this.email, this.url, this.idPat, this.view).pipe(
    //   tap(res => console.log(res)),
    //   tap(() => this.router.navigate(['/test'])),
    // )
    //   .subscribe(respuesta => {
    //     console.log("completado");
    //   });
  }

  loadFile(event: any) {
    const reader = new FileReader();
    this.file = event.target.files[0];
    reader.readAsDataURL(this.file);
    console.log(this.file);
    console.log("cargado");

    reader.onload = (_event) => {
      this.url = reader.result;
    }

  }

  openDialog(): void {
    this.dialog.open(Dialog, {
      width: '250px'
    });
  }

}

@Component({
  selector: 'dialog',
  template: `<h1 mat-dialog-title>Please read!</h1>
  <div mat-dialog-content>Execution of the model has been launched. After 5 minutes you could check your results in the results page.</div>
  <div mat-dialog-actions>
    <button mat-button mat-dialog-close>Close</button>
  </div>`,
})
export class Dialog {

  constructor(public dialogRef: MatDialogRef<Dialog>) {}

}