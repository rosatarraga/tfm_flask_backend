import { HttpClient, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { delay, map, Observable } from "rxjs";
import { Result } from "../../search/interfaces/result.interface";

@Injectable({
  providedIn: 'root'
})

export class DataService {
  private apiURL = 'http://127.0.0.1:3113';

  constructor(private http: HttpClient) {

  }

  uploadImage(email: string, image: string, idPatient:string, view:string): Observable<any> {
    const formData = new FormData();
    formData.set('image', image);
    formData.set('email', email);
    formData.set('view', view);
    formData.set('patient_id', idPatient);
    console.error(image);
    return this.http.post<any>("http://127.0.0.1:3113/uploadImage", formData);
  }

  getResults(email:string): Observable<Result[]> {
    const params = new HttpParams()
      .set('email', email);
    return this.http.get<Result[]>("http://127.0.0.1:3113/results", {params});
  }

}
