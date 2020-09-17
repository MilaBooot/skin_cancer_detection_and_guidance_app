import { Component, AfterViewInit, ViewChild } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';

@Component({
  selector: 'app-medical',
  templateUrl: './medical.component.html',
  styleUrls: ['./medical.component.css'] ,

})
export class MedicalComponent implements AfterViewInit {

  displayedColumns: string[] = [ 'name', 'hospital', 'contact'];
  dataSource = new MatTableDataSource<DoctorElement>(DOCTOR_DATA);

  @ViewChild(MatPaginator) paginator: MatPaginator;

  //need to be retrived from DB
  
  constructor() { }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
  }

}

const DOCTOR_DATA = [{name: "Ramdas", hospital: "private", contact: 123456789 }, 
                   {name: "Ramdas", hospital: "private", contact: 123456789 },
                   {name: "Ramdas", hospital: "private", contact: 123456789 },
                   {name: "Ramdas", hospital: "private", contact: 123456789 }];

export interface DoctorElement {
  name: string;
  hospital: string;
  contact: number;
 
}
