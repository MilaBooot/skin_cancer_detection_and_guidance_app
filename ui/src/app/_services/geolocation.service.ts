import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GeolocationService {
  lat;
  lng;
  zoom;
  origin;
  destination;

  constructor() {
    this.getUserLocation();
   }

   
  getUserLocation() {
    // get Users current position

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        this.lat = position.coords.latitude;
        this.lng = position.coords.longitude;
        this.zoom = 16;
        console.log("position", position)
      });
    }
  }

  getLatitude():number {
    return this.lat;
  }

  getLongitude():number {
    return this.lng;
  }
  
  async getDirection() {

    if (typeof this.lat === "undefined" || typeof this.lng === "undefined" || typeof this.zoom === "undefined") {
      await this.getUserLocation();
    }
    this.origin = { lat: this.lat, lng: this.lng };
    
    this.destination = { lat: 24.799524, lng: 120.975017 };
    console.log(this.origin);

  } 
}
