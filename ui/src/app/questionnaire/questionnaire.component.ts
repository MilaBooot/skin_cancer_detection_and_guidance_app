import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { Question, User } from '../_models';
import { AuthenticationService, QuestionnaireService } from '../_services';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.css']
})
export class QuestionnaireComponent implements OnInit {
  
  surveyQuestion: Question[];
  @Output() messageEvent = new EventEmitter<Question[]>();
  currentUser: User;

  constructor(private questionnaireService: QuestionnaireService, private authenticationService: AuthenticationService) { 
 
  }

  ngOnInit(): void {
    //intialise by invoking service
    this.currentUser = this.authenticationService.currentUserValue;

    this.questionnaireService
    .getQuestions()
    .subscribe(data => this.surveyQuestion = data);
    console.log(this.surveyQuestion);

  }

  getsurveyQuestions() {
   
    return this.surveyQuestion;
  }
/*
  sendMessage(){
    this.messageEvent.emit(this.surveyQuestion);
  }
*/

  uploadAnswers() {
    this.questionnaireService.upload(this.currentUser, this.surveyQuestion);
  }
}
