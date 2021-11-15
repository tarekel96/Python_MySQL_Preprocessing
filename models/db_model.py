import mysql.connector
import os
from db_helper import db_helper
from queries import QUERIES
# Gets the MySQL DB credentials from a .env file
from dotenv import load_dotenv
load_dotenv()

class DB_Model():
        def __init__(self): # constructor with connection path to db
                # print("in here")
                # dict containing keys with a value of a list of their respective records
                self.records = {
                        "agency": None,
                        "expedition": None,
                        "astronaut": None,
                        "astro_expedition": None
                }
                try:
                        self.connection = mysql.connector.connect(
                                # the IP Address of GCP MySQL Instance
                                host="localhost",
                                user="root",
                                password=os.getenv('password') ,
                                database="cpsc408"
                        )
                        self.cursor = self.connection.cursor()
                        print("Connection made.")
                        # print("Creating tables...")
                        # self.single_query(QUERIES["CREATE_AGENCY"])
                        # self.single_query(QUERIES["CREATE_EXPEDITION"])
                        # self.single_query(QUERIES["CREATE_ASTRONAUT"])
                        # self.single_query(QUERIES["CREATE_ASTRO_EXPED"])
                        # print("Tables have been created.")
                except mysql.connector.Error as err:
                        print(f"Error: Unable to connect to MySQL.\nPlease re-renter the password for host: localhost and user: root.")
        # assigns list of tuples to respective key of self.records dict
        def assign_table_recs(self, model_list, table_name):
                table_name = str(table_name)
                self.records[table_name] = db_helper.get_record_list(model_list)

        # function to execute fetch records
        def get_records(self,query):
                try:
                        self.cursor.execute(query)
                        results = self.cursor.fetchall()
                        results = [i[0] for i in results]
                        return results
                except Exception as err:
                        print(f"Error: An error occurred in trying execute a single query.\n{err}")

        # function for bulk inserting records
        def bulk_insert(self, query, records):
                try:
                        self.cursor.executemany(query,records)
                        self.connection.commit()
                        print("Query executed..")
                except Exception as err:
                        print(f"Error: An error occurred in trying bulk insert records.\n{err}")

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