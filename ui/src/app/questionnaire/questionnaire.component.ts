import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { Question } from '../_models';
import { QuestionnaireService } from '../_services';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.css']
})
export class QuestionnaireComponent implements OnInit {
  
  surveyQuestion: Question[];
  @Output() messageEvent = new EventEmitter<Question[]>();

  constructor(private questionnaireService: QuestionnaireService) { }

  ngOnInit(): void {
    //intialise by invoking service
    this.questionnaireService
    .getQuestions()
    .subscribe(data => this.surveyQuestion = data);
    console.log(this.surveyQuestion);
    /*
    [{id: 100, question: "Question1", options:[{id: 101, value: "A"}
    , {id: 102, value: "B"}
    , {id: 103, value: "C"}], answer:0 },
    {id: 200, question: "Question2", options:[{id: 201, value: "A"}
    , {id: 202, value: "B"}
    , {id: 203, value: "C"}], answer:0 }];
*/

  }

  getsurveyQuestions() {
   
    return this.surveyQuestion;
  }

  sendMessage(){
    this.messageEvent.emit(this.surveyQuestion);
  }

}
