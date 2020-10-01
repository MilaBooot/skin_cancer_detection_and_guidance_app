from  email_validator import validate_email, EmailNotValidError

class emailValidator():
    def is_valid(self, email_id):
        try:
            valid = validate_email(email_id)
            norm_email = valid.email
        except EmailNotValidError:
            return False
        return True
        

if __name__ == "__main__":
    validation = emailValidator()
    print(validation.is_valid("deepak@sssabcdefgh.com"))



