import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { Question } from '../_models';
import { GeolocationService } from '../_services';


@Component({
  selector: 'app-stepper',
  templateUrl: './stepper.component.html',
  styleUrls: ['./stepper.component.css']
})
export class StepperComponent implements OnInit {

  prediction = 0.0;
  isLinear = false;
  firstFormGroup: FormGroup;
  secondFormGroup: FormGroup;
  @ViewChild("fileUpload", {static: false})
  fileUpload: ElementRef;
  file: File;
  url;
  surveyQuestion: Question[];
  
  constructor(private _formBuilder: FormBuilder
    , private geolocationService: GeolocationService) {}

  ngOnInit() {
    this.firstFormGroup = this._formBuilder.group({
      firstCtrl: ['', Validators.required]
    });
    this.secondFormGroup = this._formBuilder.group({
      secondCtrl: ['', Validators.required]
    });
  }

  onClick() {  
    const fileUpload = this.fileUpload.nativeElement; 
    fileUpload.onchange = () => {  
      for (let index = 0; index < fileUpload.files.length; index++)  {  
        this.file = fileUpload.files[0];  
     }
    // this.uploadFile(); 

    };
    fileUpload.click();  
}

uploadFile() {
  //call upload service to post the request
   
    console.log(this.file.name, this.file.size);
    console.log(this.surveyQuestion);
    console.log(this.geolocationService.lat, this.geolocationService.lng);

}

onSelectFile(event) {
  if (event.target.files && event.target.files[0]) {
    var reader = new FileReader();

    reader.readAsDataURL(event.target.files[0]); // read file as data url

    reader.onload = (event) => { // called once readAsDataURL is completed
      this.url = event.target.result;
    }
  }
}

receiveMessage($event) {
  this.surveyQuestion = $event
}



}

