import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Question, User } from '../_models';
import { first } from 'rxjs/operators';
import { AlertService } from './alert.service';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class QuestionnaireService {


  constructor(private http: HttpClient, private alertService: AlertService) { }

  getQuestions():Observable<Question[]> {
    return this.http.get(environment.baseUrl + '/bff/api/questionnaire')
    .pipe(map(result=> {
      console.log(result['questions']);
      return result['questions']}));
}

  upload(user: User, surveyAnswers: Question[]) {
    console.log(user.username);
    return this.http.post(environment.baseUrl + '/bff/api/questionnaire-reponse/'+ encodeURIComponent(user.username) + '/upload', {
      questions: surveyAnswers}) .pipe(first())
      .subscribe(
          data => {
          },
          error => {
             this.alertService.error(error);
          });

  }


}
