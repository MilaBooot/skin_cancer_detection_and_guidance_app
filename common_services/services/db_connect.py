import psycopg2
import logging
import json
import os
from geopy.geocoders import Nominatim


DB_SERVER = os.environ.get("RDS_HOSTNAME")

class dbConnect:
    def __init__(self):
        try:
            self.db = psycopg2.connect(dbname="app_db", user="postgres", 
                                       host=DB_SERVER, password="postgres")
            self.cur = self.db.cursor()
        except Exception as errmsg:
            raise Exception("Login failed %s" %errmsg)
        
    def get_login_creds(self, user_id):
        query = """SELECT password FROM app_data.user_details WHERE user_id='%s'""" % (user_id,)
        self.cur.execute(query)
        password = self.cur.fetchall()
        if len(password) > 0:
            password = password[0][0]
        else:
            raise KeyError("User ID does not exist")
        return password

    def get_user_details(self, user_id):
        query = """SELECT * FROM app_data.user_details WHERE user_id='%s'""" % (user_id,)
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
        self.cur.execute("""SELECT user_id FROM app_data.user_details""")
        user_ids = self.cur.fetchall()
        user_ids = [uid[0] for uid in user_ids]
        return user_ids

    def insert_value(self, user_id, password, first_name, last_name, dob, gender):
        try:
            insert_query = """INSERT INTO app_data.user_details (user_id, password, first_name, last_name, dob, gender) VALUES (%s, %s, %s, %s, %s, %s)"""
            to_insert = (user_id, password, first_name, last_name, dob, gender)
            self.cur.execute(insert_query, to_insert)
            self.db.commit()
            count = self.cur.rowcount
        except Exception as errmsg:
            print(errmsg)
            self.db.rollback()
            raise Exception("DB insert operation failed")
        return ("%s Record inserted successfully into user_registration table" % count)

    def get_questions(self, id=None):
        ret = []
        if id is None:
            self.cur.execute("""SELECT * FROM app_data.questionnaire""")
        else:
            self.cur.execute("""SELECT * FROM app_data.questionnaire WHERE id='%s'""" % (id,))
        questions = self.cur.fetchall()
        for question in questions:
            options = self.get_options(question[2])
            data = {"id": question[0],
                    "question": question[1],
                    "options": options,
                    "answer": 0}
            ret.append(data)
        if len(ret) == 0:
            raise KeyError()
        return ret

    def get_options(self, ans_ids):
        ret = []
        if not isinstance(ans_ids, list):
            ans_ids = [ans_ids]
        for id in ans_ids:
            self.cur.execute("""SELECT * FROM app_data.answers WHERE id='%s'""" % (id,))
            answer = self.cur.fetchall()
            answer = {"id":id, "value": answer[0][1]}
            ret.append(answer)
        if len(ret) == 0:
            raise KeyError()
        return ret

    def get_doctors(self, lat, long):
        ret_data = []
        geolocator = Nominatim(user_agent="custom_name")
        coordinates = "%s, %s" % (lat, long)
        location = geolocator.reverse(coordinates)
        city = location.raw["address"]["city"]
        self.cur.execute("""SELECT * FROM app_data.doctors WHERE city='%s'""" % (city,))
        doctors = self.cur.fetchall()      
        for doctor in doctors:
            hospital = ", " .join([doctor[2], doctor[7], doctor[3], doctor[5], str(doctor[6])])
            data = {"name": doctor[1], "speciality": doctor[4], "hospital": hospital, "latitude": "9.9312", 
                    "longitude": "76.2673"}
            ret_data.append(data)
        return ret_data

    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    #testing function
    from pprint import pprint
    ldb = dbConnect()
    pprint(ldb.get_doctors(9.9312, 76.2673))
    #password = ldb.get_questions(1)
    #print(password)

