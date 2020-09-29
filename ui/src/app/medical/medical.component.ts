import { Component, AfterViewInit, ViewChild, OnInit, ElementRef  } from '@angular/core';
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
  doctorList: Doctor[];
  lat;
  lng;

  @ViewChild('mapContainer', {static: false}) gmap: ElementRef;

  map: google.maps.Map;
  
  coordinatesArray: google.maps.LatLng[] = [];
  marker:google.maps.Marker;
 


  mapInitializer() {

    let userCoordinates = new google.maps.LatLng(this.lat, this.lng);
    let mapOptions: google.maps.MapOptions = {
    center: userCoordinates,
    zoom: 10,
  };
    this.map = new google.maps.Map(this.gmap.nativeElement, 
    mapOptions);

    this.marker = new google.maps.Marker({
      position: userCoordinates,
      map: this.map,
      title: "You"
    });
    this.marker.setMap(this.map);

   console.log(this.doctorList);
  
   this.doctorList.forEach(doc => {
    let gcoordinates = new google.maps.LatLng(doc.latitude, doc.longitude);
    let hosMarker = new google.maps.Marker({
      position: gcoordinates,
      map: this.map,
      title: doc.name,
    });
    console.log(doc.name);
    hosMarker.setMap(this.map);

  });

   
   }
  
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
      this.mapInitializer();
     
    } );
  
  }

  ngAfterViewInit() {
    
    setTimeout(() => {
      console.log('sleep');
      this.doctorDataSource.paginator = this.paginator;
      
    }, 100);
      
 
  }

}

