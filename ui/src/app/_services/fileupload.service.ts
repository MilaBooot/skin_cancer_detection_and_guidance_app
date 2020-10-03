import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'; 
import {  
  HttpClient,  
  HttpHeaders  
} from '@angular/common/http'; 
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FileuploadService {

 
  constructor(private http: HttpClient) {}  

  public downloadFile(docFile: string, username: string): Observable < Blob > {  
      return this.http.get(environment.baseUrl + '/bff/api/' +  encodeURIComponent(username)  + '/getDocument?docFile=' + docFile, {  
        responseType: 'blob'  
    });    
  }  
  
  public downloadImage(image: string): Observable < Blob > {  
      return this.http.get(environment.baseUrl + '/GetImage?image=' + image, {  
          responseType: 'blob'  
      });  
  } 


  public getFiles(username): Observable < any[] > {  
      return this.http.get < any[] > (environment.baseUrl + '/bff/api/' + encodeURIComponent(username) + '/getDocuments');  
  }  
  public AddFileDetails(data: FormData): Observable < string > {  
      
      return this.http.post < string > (environment.baseUrl + '/bff/api/uploadDocument', data);  
  }  

  public deleteDocument(docFile: string, username: string): Observable<any> {
    return this.http.delete(environment.baseUrl + '/bff/api/' +  encodeURIComponent(username)  + '/document?docFile=' + docFile); 
  }
}
