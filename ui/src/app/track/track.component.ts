import { Component, OnInit, ViewChild,  AfterViewInit} from '@angular/core';
import { saveAs as importedSaveAs } from "file-saver";  
import { FileuploadService } from '../_services/fileupload.service';  
import {  Validators, FormBuilder } from '@angular/forms';
import { AuthenticationService } from '../_services';

@Component({
  selector: 'app-track',
  templateUrl: './track.component.html',
  styleUrls: ['./track.component.css']
})
export class TrackComponent implements OnInit {

  @ViewChild('documentInput', {  
    static: true  
}) prescriptionInput;  

selectedFile: File = null;  
fileToUpload: File = null;  
saveFileForm: any;  
lstFileDetails: any;
user: any;
constructor(private service: FileuploadService
  , private formBuilder: FormBuilder
  , private authenticationService: AuthenticationService) {}  

ngOnInit(): void {  
   
    this.saveFileForm = this.formBuilder.group({  
      Description: ['', [Validators.required]]  
    });  
    this.authenticationService.currentUser.subscribe(data => {this.user = data.username});
    this.service.getFiles(this.user).subscribe(result => {  
    this.lstFileDetails = result;  
    }) ;
} 
  

downloadDocFile(data) {  
    const DocFileName = data.filename;  
    var DocFile = DocFileName;  
    this.service.downloadFile(DocFile, this.user).subscribe((data) => { 
        console.log(data);
      
       let blob = new Blob([data]); 
        importedSaveAs(blob, DocFile)  
    });  
}  

onSelectFile(file: FileList) {  
    this.fileToUpload = file.item(0);  
    var reader = new FileReader();  
    reader.readAsDataURL(this.fileToUpload);  
}  

downloadImage(data) {  
    const ImageName = data.ImageName;  
    var image = ImageName.slice(0, -4);  
    this.service.downloadImage(image).subscribe((data) => {  
        importedSaveAs(data, image)
    });  
}  

deleteDocFile(data) {

    const DocFileName = data.filename;  
    console.log(DocFileName);
    var DocFile = DocFileName;  
    this.service.deleteDocument(DocFile, this.user).subscribe((data) => {
        console.log("removed file successfully");
    }); 
}

onExpSubmit() {  
    debugger;  
    if (this.saveFileForm.invalid) {  
        return;  
    } 
    
    let formData = new FormData();  
    formData.append('file', this.prescriptionInput.nativeElement.files[0]);  
    formData.append('description', this.saveFileForm.value.Description);  
    formData.append('username', this.user)
    this.service.AddFileDetails(formData).subscribe(result => {});  
} 
}
