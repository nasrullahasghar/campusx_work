import mysql.connector
import sys

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user='root',password='',database='hit_db_demo')
            self.mycursor = self.conn.cursor()
        except:
            print("Some Error occoured,Cannot connect to database")
            sys.exit(0)
            
        else:
            print("Connected to database")


    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        

    def search(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.mycursor.execute(query, (email, password))
        return self.mycursor.fetchall()

