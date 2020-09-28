import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-contactus',
  templateUrl: './contactus.component.html',
  styleUrls: ['./contactus.component.css']
})
export class ContactusComponent implements OnInit {

  public data:any=[];
  name; email; mobile; subject; message;
 
  
  constructor(){
  }

  ngOnInit(): void {

  }
 
  save(): void {
    this.data['name']= this.name;
                this.data['email']= this.email;
                this.data['mobile']= this.mobile;
                this.data['subject']= this.subject;
                this.data['message']= this.message;
    console.log(this.data);
    //invoke service to send feedback

   }

}
