import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { Question, User , Prediction} from '../_models';
import { AlertService, AuthenticationService, GeolocationService, UserService } from '../_services';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-stepper',
  templateUrl: './stepper.component.html',
  styleUrls: ['./stepper.component.css']
})
export class StepperComponent implements OnInit {

  predictionModel : Prediction = null;
  isLinear = false;
  firstFormGroup: FormGroup;
  secondFormGroup: FormGroup;
  @ViewChild("fileUpload", {static: false})
  fileUpload: ElementRef;
  file: File;
  url;
  currentUser: User;
  surveyQuestion: Question[];
  width;
  height;


  
  constructor(private _formBuilder: FormBuilder
    , private userService : UserService
    , private authenticationService: AuthenticationService
    , private alertService: AlertService) {}

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
  
  };
 
    fileUpload.click();  
}

reset() {
  this.userService.setCancerDetected("no");
}
uploadFile() {
  //call upload service to post the request
    const uploadData = new FormData();
    uploadData.append("image", this.file, this.file.name);
    this.userService.upload(uploadData, this.currentUser)
    .pipe(first())
    .subscribe(
        data => {
           this.predictionModel = data;
           this.userService.setCancerDetected(this.predictionModel.cancer);
           this.userService.setImageProcessed();
        },
        error => {
            this.alertService.error(error);
          
        });;

    

}

 isEmpty():boolean {
   if (this.predictionModel == null) {
     return true;
   } else {
     return false;
   }
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

