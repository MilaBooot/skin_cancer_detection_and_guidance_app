import { Injectable } from '@angular/core';
import { HttpClient, HttpRequest } from '@angular/common/http';
import { Prediction, User } from '../_models';
import { map } from 'rxjs/operators';
import { AlertService } from './alert.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient, private alertService: AlertService) { }

  register(user: User) {
    console.log(user);
    return this.http.post(`/bff/api/register`, user);
}

  upload(uploadForm: FormData, user: User):Observable<Prediction> {
  
    return this.http.post<Prediction>(`/bff/api/image/`+ encodeURIComponent(user.username) + `/upload`, uploadForm)
    .pipe(map( result => {
      console.log(result);
      return result}));
  }

  
}
