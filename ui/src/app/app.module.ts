import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RegisterComponent } from './register/register.component';
import { AlertComponent } from './_components';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { StepperComponent } from './stepper/stepper.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatStepperModule } from '@angular/material/stepper';
import { MedicalComponent } from './medical/medical.component';
import { PolicyComponent } from './policy/policy.component';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatTableModule} from '@angular/material/table';
import { SocialLoginModule, SocialAuthServiceConfig } from 'angularx-social-login';
import {GoogleLoginProvider} from 'angularx-social-login';


 


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    AlertComponent,
    HomeComponent,
    AboutComponent,
    StepperComponent,
    MedicalComponent,
    PolicyComponent,
    QuestionnaireComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatInputModule,
    MatStepperModule,
    MatIconModule,
    MatButtonModule,
    MatPaginatorModule,
    MatTableModule,
    SocialLoginModule


  ],
  providers: [ {
    provide: 'SocialAuthServiceConfig',
    useValue: {
      autoLogin: false,
      providers: [
        {
          id: GoogleLoginProvider.PROVIDER_ID,
          provider: new GoogleLoginProvider(
            '1005663427262-0thkv1hfrufo4rqsc2eph7u7bt3v5i2f.apps.googleusercontent.com'
          ),
        }
      ],
    } as SocialAuthServiceConfig,
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
