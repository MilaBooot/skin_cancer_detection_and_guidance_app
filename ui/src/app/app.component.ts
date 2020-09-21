import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { User } from './_models';
import { AuthenticationService, UserService } from './_services';

@Component({
  selector: 'app',
  templateUrl: './app.component.html'
})
export class AppComponent {
  title = 'skin-cancer-detection-ui';
  currentUser: User;

    constructor(
        private router: Router,
        private authenticationService: AuthenticationService,
        private userService: UserService
    ) {
        this.authenticationService.currentUser.subscribe(x => this.currentUser = x);
    }

    logout() {
        this.authenticationService.logout();
        this.router.navigate(['/login']);
    }

    check(): boolean {
      return this.userService.isCancerDetected();
    }
}
