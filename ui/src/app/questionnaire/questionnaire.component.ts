import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { Question } from '../_models';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.css']
})
export class QuestionnaireComponent implements OnInit {
  
  surveyQuestion: Question[];
  @Output() messageEvent = new EventEmitter<Question[]>();

  constructor() { }

  ngOnInit(): void {
    //intialise by invoking service
    this.surveyQuestion = [{id: 100, question: "Question1", options:[{id: 101, option: "A"}
    , {id: 102, option: "B"}
    , {id: 103, option: "C"}], answer:0 },
    {id: 200, question: "Question2", options:[{id: 201, option: "A"}
    , {id: 202, option: "B"}
    , {id: 203, option: "C"}], answer:0 }];


  }

  getsurveyQuestions() {
    return this.surveyQuestion;
  }

  sendMessage(){
    this.messageEvent.emit(this.surveyQuestion);
  }

}
