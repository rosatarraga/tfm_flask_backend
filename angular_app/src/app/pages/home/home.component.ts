import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DataService } from 'src/app/pages/home/services/data.service';
import { FileValidator } from 'ngx-material-file-input';
import { tap } from 'rxjs';

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
    private _formBuilder: FormBuilder,
    private dataService: DataService,
    private router: Router,
  ) { }

  ngOnInit(): void {

  }


  processFile() {
    this.dataService.uploadImage(this.email, this.url).pipe(
      tap(res => console.log(res)),
      tap(() => this.router.navigate(['/test'])),
    )
      .subscribe(respuesta => {
        console.log("completado");
      });

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


}
