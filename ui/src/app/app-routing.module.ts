
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login';
import { RegisterComponent } from './register';
import { HomeComponent } from './home';
import { AboutComponent } from './about';
import { AuthGuard } from './_helpers';
import { PolicyComponent } from './policy/policy.component';
import { TrackComponent } from './track/track.component';
import { MedicalComponent } from './medical';
import { ContactusComponent } from './contactus/contactus.component';

const routes: Routes = [
  { path: '', component: HomeComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'about', component: AboutComponent, canActivate: [AuthGuard] }, 
  { path: 'info', component: PolicyComponent, canActivate: [AuthGuard] }, 
  { path: 'track', component: TrackComponent, canActivate: [AuthGuard] }, 
  { path: 'medical', component: MedicalComponent, canActivate: [AuthGuard] }, 
  { path: 'contactus', component: ContactusComponent }, 
  // otherwise redirect to home
  { path: '**', redirectTo: '' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
