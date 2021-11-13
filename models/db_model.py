import mysql.connector
import os
# Gets the MySQL DB credentials from a .env file
from dotenv import load_dotenv
load_dotenv()

class DB_Model():
        def __init__(self): # constructor with connection path to db
                print("in here")
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
    
#     # Check if the songs table is made or not
#     def table_exists(self, table_name = "songs", create_table = True):
#         query = '''
#         SELECT count(name) FROM sqlite_master WHERE type='table' AND name=:table_name 
#         '''
#         dictionary = {"table_name": table_name}
#         #get the count of tables with the name
#         self.cursor.execute(query, dictionary)
#         res = self.cursor.fetchone()[0]
#         if res == 0:
#             print(f"A table with the name {table_name} does not exist.")
#             if create_table == True:
#                 self.create_table(table_name)
#         if res == 1:
#             print(f"A table with the name {table_name} exists.")
    
#     def create_table(self, table_name = "songs"):
#         print(f"Creating {table_name} table...")
#         query = f'''
#         CREATE TABLE {table_name}(
#         songID VARCHAR(22) NOT NULL PRIMARY KEY,
#         Name VARCHAR(20),
#         Artist VARCHAR(20),
#         Album VARCHAR(20),
#         releaseDate DATETIME,
#         Genre VARCHAR(20),
#         Explicit BOOLEAN,
#         Duration DOUBLE,
#         Energy DOUBLE,
#         Danceability DOUBLE,
#         Acousticness DOUBLE,
#         Liveness DOUBLE,
#         Loudness DOUBLE
#         ); 
#         '''
#         dictionary = {"table_name": table_name}
#         self.cursor.execute(query, dictionary)
#         print(f"{table_name} table successfully made.")

#     # function for bulk inserting records
#     def bulk_insert(self,query,records):
#         self.cursor.executemany(query,records)
#         self.connection.commit()
#         print("query executed..")

#     def update_records(self, query, dictionary):
#         self.cursor.execute(query, dictionary)
#         self.connection.commit()
#         print("update successfully processed...")

#     # function to return a single value from table
#     def single_record(self,query):
#         self.cursor.execute(query)
#         # cusor will return a tuple, the index 0 is because we know it should only be one value (count)
#         return self.cursor.fetchone()[0]

#     # function to return a single row based on the options from the dictionary
#     def single_record_options(self, query, dictionary):
#         self.cursor.execute(query, dictionary)
#         return self.cursor.fetchall()[0]
    
#         # function to return all rows based on the options from the dictionary
#     def get_records_options(self, query, dictionary):
#         self.cursor.execute(query, dictionary)
#         return self.cursor.fetchall()
    
#     def get_record_col_names(self, query, dictionary={}):
#         self.cursor.execute(query, dictionary)
#         # Get col names from description tuples
#         return [description[0] for description in self.cursor.description]

#     # function to return a single attribute values from table
#     def single_attribute(self,query):
#         self.cursor.execute(query)
#         results = self.cursor.fetchall()
#         results = [i[0] for i in results]
#         if None in results:
#             results.remove(None)
#         return results

#     # SELECT with named placeholders
#     def name_placeholder_query(self,query,dictionary):
#         self.cursor.execute(query,dictionary)
#         results = self.cursor.fetchall()
#         results = [i[0] for i in results]
#         return results