import psycopg2


class loginDBConnect:
    def __init__(self):
        try:
            self.db = psycopg2.connect(dbname="app_login", user="postgres", host="localhost", password="postgres")
            self.cur = self.db.cursor()
        except Exception as errmsg:
            print("Login failed %s" %errmsg)
        
    def get_login_creds(self):
        self.cur.execute("""SELECT * FROM user_registration""")
        rows = self.cur.fetchall()
        return rows
    
    def get_user_ids(self):
        self.cur.execute("""SELECT user_id FROM user_registration""")
        user_ids = self.cur.fetchall()
        user_ids = [uid[0] for uid in user_ids]
        return user_ids

    def insert_value(self, user_id, password, first_name, last_name, dob, gender):
        insert_query = """INSERT INTO user_registration (user_id, password, first_name, last_name, dob, gender) VALUES (%s, %s, %s, %s, %s, %s)"""
        to_insert = (user_id, password, first_name, last_name, dob, gender)
        self.cur.execute(insert_query, to_insert)
        self.db.commit()
        count = self.cur.rowcount
        return ("%s Record inserted successfully into user_registration table" % count)

    def __del__(self):
        self.db.close()


if __name__ == "__main__":
    #testing function
    ldb = loginDBConnect()
    uids = ldb.get_user_ids()
    print(uids)