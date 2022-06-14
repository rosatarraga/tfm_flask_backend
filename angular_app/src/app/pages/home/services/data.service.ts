import { HttpClient, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { delay, map, Observable } from "rxjs";
import { Result } from "../../search/interfaces/result.interface";

@Injectable({
  providedIn: 'root'
})

export class DataService {
  private apiURL = 'http://localhost:5000';

  constructor(private http: HttpClient) {

  }

  uploadImage(email: string, image: File, idPatient:string, view:string): Observable<any> {
    const formData = new FormData();
    formData.set('image', image);
    formData.set('email', email);
    formData.set('view', view);
    formData.set('patient_id', idPatient);
    return this.http.post<any>("http://localhost:5000/uploadImage", formData);
  }

  getResults(email:string): Observable<Result[]> {
    const params = new HttpParams()
      .set('email', email);
    return this.http.get<Result[]>("http://localhost:5000/results", {params});
  }

}
