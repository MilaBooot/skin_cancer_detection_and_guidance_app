import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { Question, User } from '../_models';
import { AuthenticationService, GeolocationService, UserService } from '../_services';


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
  currentUser: User;
  surveyQuestion: Question[];
  
  constructor(private _formBuilder: FormBuilder
    , private geolocationService: GeolocationService
    , private userService : UserService
    , private authenticationService: AuthenticationService) {}

  ngOnInit() {
    this.currentUser = this.authenticationService.currentUserValue;
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
    const uploadData = new FormData();
    uploadData.append("image", this.file, this.file.name);
    this.userService.upload(uploadData, this.currentUser);

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

/*
receiveMessage($event) {
  this.surveyQuestion = $event
}

*/

}

