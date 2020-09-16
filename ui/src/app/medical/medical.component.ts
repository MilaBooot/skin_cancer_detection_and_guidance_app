import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-medical',
  templateUrl: './medical.component.html'
})
export class MedicalComponent implements OnInit {

  //need to be retrived from DB
  doctorDetails = [{name: "Ramdas", hospital: "private", contact: 123456789 }, 
                   {name: "Ramdas", hospital: "private", contact: 123456789 },
                   {name: "Ramdas", hospital: "private", contact: 123456789 },
                   {name: "Ramdas", hospital: "private", contact: 123456789 }];
  constructor() { }

  ngOnInit(): void {
  }

}
