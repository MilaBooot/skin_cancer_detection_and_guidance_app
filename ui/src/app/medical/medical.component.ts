import { Component, AfterViewInit, ViewChild, OnInit } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';
import { Doctor } from '../_models';
import { GeolocationService, UserService } from '../_services';

@Component({
  selector: 'app-medical',
  templateUrl: './medical.component.html',
  styleUrls: ['./medical.component.css'] ,

})
export class MedicalComponent implements AfterViewInit, OnInit {

  displayedColumns: string[] = [ 'name', 'speciality', 'hospital'];
  dataSource;
  doctorList: Doctor[];
  lat = 27.1751;
  lng = 78.0421;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  //need to be retrived from DB
  
  constructor(private userService: UserService) {
    this.userService.getDoctorInfo()
    .subscribe(data => this.doctorList = data);
    this.dataSource = new MatTableDataSource<Doctor>(this.doctorList);
   }
  ngOnInit(): void {
      
    
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
  }

}

