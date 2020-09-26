export class User {
    username: string;
    password: string;
    firstname: string;
    lastname: string;
    gender:string;
    dob:string

    constructor(username, firstname) {
        this.username = username;
        this.firstname = firstname;

    }
}
