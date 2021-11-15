# Python_MySQL_Preprocessing
## Author: Tarek El-Hajjaoui

## Description of Program
- A Python program that connects to MySQL db hosted on GCP and creates tables based based on sql_queries.sql. **The program contains the bonus**:
- Implement the code to ensure that data is inserted correctly with the AUTO_INCREMENT 
constraint set in place for tables, without using a staging table. That is, insert data into 
agency table first. Then load up the auto generated IDs for each agency back into Python to 
then combine with astronaut data (for foreign key) and insert that into the astronaut table. 
Do the same with the expedition and astro_expedition tables data. 

# IMPORTANT: Before running the program:
1. Install the pip requirements via: 
```
pip3 install -r requirements
``` 
2. Create a .env file (the IP Address of the GCP Instance is protected because the code is on my GitHub):
```
touch .env
``` 
3. Inside the .env file, create this variable:
```
hostname=IpAddress
```
- Where IpAddress is the ip address provided on Canvas

## Instructions to run the program:
1. Complete steps above.
2. Run the program with this command:
```
python3 app.py
```

## Source Files:
- app.py
- agency.py
- astro_expedition.py
- astronaut.py
- db_model.py
- expedtion.py
- parser.py
- staging_model.py
- db_helper.py
- expeditionData.csv
- README.md

## Sources referred to:
- mysql python connector: https://dev.mysql.com/doc/connector-python/en/
- Python built-in enumerate: https://docs.python.org/3/library/functions.html#enumerate
- Python with statement: https://www.geeksforgeeks.org/with-statement-in-python/#:~:text=with%20statement%20in%20Python%20is,common%20resources%20like%20file%20streams.


Steps for the solution:
1) Load expeditionData.csv file 
2) Create agency instances by reading file
3) Insert agency records into db
4) Retrieve agency records from db to assign agency IDs
5) Create expedition, astronaut, and astronaut_expedtion instances by reading file
6) Insert expedition and astronaut records
7) Insert astronaut_expedition records

## Original Assignment Instructions:
Overview  
 
Rework the data loading process for the expeditionData.csv file using Python instead of 
pure SQL statements. 
 
Details 
 
You will rely on the mysql-connector-python library to connect your cloud MySQL instance 
to Python and insert relevant data into the four tables. Instead of creating a staging table 
and running SQL queries to insert data, you will first load the data file in Python and 
programmatically split it into chunks of data that can be inserted into the agency, 
expedition, astronaut, and astro_expedition tables in the cpsc408 database.  
 
For ease, you can recreate your tables without the AUTO_INCREMENT constraint which 
will make it easy to generate IDs of your own and insert data into tables without the need 
for joining. The foreign key references, however, will remain the same. 
 
I am presenting steps for one of the solutions you can implement for this assignment: 
1)  Load expeditionData.csv file 
2)  Break records into 3 chunks: agency info, astronaut info, expedition info. 
3)  Generate an ID for each record in the 3 chunks 
4)  Insert data into agency, expedition, astronaut tables. 
5)  Using the IDs generated, insert data into astro_expedition table. 
 
 
Bonus (20 points) 
 
Implement the code to ensure that data is inserted correctly with the AUTO_INCREMENT 
constraint set in place for tables, without using a staging table. That is, insert data into 
agency table first. Then load up the auto generated IDs for each agency back into Python to 
then combine with astronaut data (for foreign key) and insert that into the astronaut table. 
Do the same with the expedition and astro_expedition tables data. 
 
 
This assignment is to be implemented in your cloud instance of MySQL. Create a new User 
on GCP with name rao and password password1. In your README, share your instance’s 
Public IP address so I may run your code efficiently. Also specify in README if you are 
attempting the Bonus version of the program. 
 
Ensure that you implement object-oriented programming in your program. Add comments 
where necessary. Points will be deducted for poor OOP and coding practices. 