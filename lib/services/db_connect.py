import psycopg2


class loginDBConnect:
    def __init__(self):
        try:
            self.db = psycopg2.connect(dbname="app_login", user="postgres", host="localhost", password="postgres")
            self.cur = self.db.cursor()
        except Exception as errmsg:
            print("Login failed %s" %errmsg)
        
    def get_login_creds(self, user_id):
        query = """SELECT password FROM user_registration WHERE user_id='%s'""" % (user_id,)
        self.cur.execute(query)
        password = self.cur.fetchall()
        if len(password) > 0:
            password = password[0][0]
        else:
            raise KeyError("User ID does not exist")
        return password

    def get_user_details(self, user_id):
        query = """SELECT * FROM user_registration WHERE user_id='%s'""" % (user_id,)
        self.cur.execute(query)
        result = self.cur.fetchall()
        if len(result) > 0:
            ret = {"first_name": result[0][2],
                   "last_name": result[0][3],
                   "password": result[0][1],
                   "dob": str(result[0][4]),
                   "gender": result[0][5]}
        else:
            raise KeyError("User ID does not exist")
        return ret
    
    def get_user_ids(self):
        self.cur.execute("""SELECT user_id FROM user_registration""")
        user_ids = self.cur.fetchall()
        user_ids = [uid[0] for uid in user_ids]
        return user_ids

    def insert_value(self, user_id, password, first_name, last_name, dob, gender):
        try:
            insert_query = """INSERT INTO user_registration (user_id, password, first_name, last_name, dob, gender) VALUES (%s, %s, %s, %s, %s, %s)"""
            to_insert = (user_id, password, first_name, last_name, dob, gender)
            self.cur.execute(insert_query, to_insert)
            self.db.commit()
            count = self.cur.rowcount
        except Exception:
            self.db.rollback()
            raise Exception("DB insert operation failed")
        return ("%s Record inserted successfully into user_registration table" % count)

    def __del__(self):
        self.db.close()


if __name__ == "__main__":
    #testing function
    ldb = loginDBConnect()
    password = ldb.get_user_details("deepak46@gmail.com")
    print(password)
