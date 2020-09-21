import { Injectable } from '@angular/core';
import { HttpClient, HttpRequest } from '@angular/common/http';
import { Doctor, Prediction, User } from '../_models';
import { map } from 'rxjs/operators';
import { AlertService } from './alert.service';
import { Observable } from 'rxjs';
import { GeolocationService } from './geolocation.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  isCancer: boolean = false;
  cancerDetected = "No";
  isImageProcessed = false;

  constructor(private http: HttpClient
    , private alertService: AlertService
    , private geolocationService: GeolocationService) { }

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

  getDoctorInfo():Observable<Doctor[]> {
    return this.http.get<Doctor[]>(`/bff/api/doctors/`+ encodeURIComponent(this.geolocationService.getLongitude())
     + `/` + encodeURIComponent(this.geolocationService.getLatitude()))
    .pipe(map( result => {
      console.log(result['doctors']);
      return result['doctors']}));
  }

  setCancerDetected(reponse: string) {
    this.cancerDetected = reponse;
  }

  setImageProcessed() {
    this.isImageProcessed = true;
  }

  checkImageProcessed(): boolean {
    return this.isImageProcessed;
  }

  isCancerDetected(): boolean {
    if(this.cancerDetected == "yes") {
      this.isCancer = true;
    }
    return this.isCancer;

  }

  
}
