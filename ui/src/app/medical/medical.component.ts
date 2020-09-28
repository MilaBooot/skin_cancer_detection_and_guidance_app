import { Component, AfterViewInit, ViewChild, OnInit } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';
import { Doctor } from '../_models';
import { GeolocationService, UserService } from '../_services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-medical',
  templateUrl: './medical.component.html',
  styleUrls: ['./medical.component.css'] ,

})
export class MedicalComponent implements AfterViewInit, OnInit {

  displayedColumns: string[] = [ 'name', 'speciality', 'hospital', 'action'];
  doctorDataSource;
  doctorList: any[];
  lat;
  lng;
  
  @ViewChild(MatPaginator) paginator: MatPaginator;

  //need to be retrived from DB
  
  constructor(private userService: UserService
    , private geolocationService: GeolocationService) {
      
    this.lat = geolocationService.lat;
    this.lng = geolocationService.lng; 
    
  }

  ngOnInit(): void {
    this.userService.getDoctorInfo(this.lat, this.lng)
    .pipe(first())
    .subscribe(data =>{
      this.doctorList = data;
      this.doctorDataSource = new MatTableDataSource<Doctor>(this.doctorList);
     
    } );
  
  }

  ngAfterViewInit() {
    
    setTimeout(() => {
      console.log('sleep');
      this.doctorDataSource.paginator = this.paginator;
    }, 100);
        
 
  }

}

