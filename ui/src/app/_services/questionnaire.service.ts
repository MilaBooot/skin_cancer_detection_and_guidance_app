import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Question } from '../_models';

@Injectable({
  providedIn: 'root'
})
export class QuestionnaireService {


  constructor(private http: HttpClient) { }

  getQuestions():Observable<Question[]> {
    return this.http.get(`/bff/api/questionnaire`)
    .pipe(map(result=> {
      console.log(result['questions']);
      return result['questions']}));
}


}
