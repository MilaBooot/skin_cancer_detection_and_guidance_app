import { Injectable } from '@angular/core';
import { HttpClient, HttpRequest } from '@angular/common/http';
import { Question, User } from '../_models';
import { first } from 'rxjs/operators';
import { AlertService } from './alert.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient, private alertService: AlertService) { }

  register(user: User) {
    console.log(user);
    return this.http.post(`/bff/api/register`, user);
}

  upload(uploadForm: FormData, user: User) {
  
    return this.http.post(`/bff/api/image/`+ encodeURIComponent(user.username) + `/upload`, uploadForm)
    .pipe(first())
    .subscribe(
        data => {
          
        },
        error => {
          this.alertService.error(error);
        });
  }

  
}
