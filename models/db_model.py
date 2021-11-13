import mysql.connector
import os
# Gets the MySQL DB credentials from a .env file
from dotenv import load_dotenv
load_dotenv()

class DB_Model():
        def __init__(self): # constructor with connection path to db
                # print("in here")
                try:
                        self.connection = mysql.connector.connect(
                                # the IP Address of GCP MySQL Instance
                                host="localhost",
                                user="root",
                                password=os.getenv('password') 
                        )
                        self.cursor = self.connection.cursor()
                        print("Connection made..")
                except mysql.connector.Error as err:
                        print(f"Error: Unable to connect to MySQL.\nPlease re-renter the password for host: localhost and user: root.")

       # close connection 
        def destructor(self):
                self.connection.close()

        '''
        # order of table creation
          1) AGENCY
          2) EXPEDITION
          3) ASTRONAUT relies --> AGENCY
          4) ASTRO_EXP relies --> EXPEDITION & ASTRONAUT

        '''