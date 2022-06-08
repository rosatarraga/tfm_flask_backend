import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { delay, map, Observable } from "rxjs";

@Injectable({
  providedIn: 'root'
})

export class DataService {
  private apiURL = 'http://localhost:5000';

  constructor(private http: HttpClient) {

  }

  uploadImage(email: string, image: File): Observable<any> {
    const formData = new FormData();
    formData.set('image', image);
    formData.set('email', email);
    console.log('llamando service');
    console.log(formData);
    return this.http.post<any>("http://localhost:5000/uploadImage", formData);
  }

}
