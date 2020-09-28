import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Doctor, Prediction, User } from '../_models';
import { map } from 'rxjs/operators';
import { AlertService } from './alert.service';
import { Observable } from 'rxjs';
import { GeolocationService } from './geolocation.service';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  isCancer: boolean = false;
  cancerDetected = "No";
  isImageProcessed = false;



  constructor(private http: HttpClient
    , private alertService: AlertService) {
    
     
     }

  register(user: User) {
    console.log(user);

    return this.http.post(environment.baseUrl + '/bff/api/register' , user);
}

  upload(uploadForm: FormData, user: User):Observable<Prediction> {
  
    return this.http.post<Prediction>(environment.baseUrl + '/bff/api/image/'+ encodeURIComponent(user.username) + '/upload', uploadForm)
    .pipe(map( result => {
      console.log(result);
      return result}));
  }

  getDoctorInfo(lat: number, lng: number):Observable<Doctor[]> {
  
    return this.http.get<Doctor[]>(environment.baseUrl + '/bff/api/doctors/' + encodeURIComponent(lng)
     + '/' + encodeURIComponent(lat))
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
