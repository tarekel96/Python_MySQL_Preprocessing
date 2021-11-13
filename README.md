# Python_MySQL_Preprocessing

Steps for the solution:
1)  Load expeditionData.csv file 
2)  Break records into 3 chunks: agency info, astronaut info, expedition info. 
3)  Generate an ID for each record in the 3 chunks 
4)  Insert data into agency, expedition, astronaut tables. 
5)  Using the IDs generated, insert data into astro_expedition table.

Hints:
1) Run the CREATE TABLE queries given using DataGrap to create the tables into the MySQL Database.
2) Do not use the Autoincrement part
3) 3 different lists of tuples
        3a) [(agencyName), (agencyOrganization)]
        3b) [(astronautName), (astronautAge), (agencyName)]
        3c) [(expeditionNumber), (astronautNumber)]
        Note: These lists may have repeating instances, check for that.
<!-- Replace the dict values with actual numbers from the lists -->
dict - {
        agencyName: ,

}
for example,
        Alist = [('a', 'US'), ('B', 'US')]
        d[i[0]] = counter where the key is 
                [('a', 'US'), ('B', 'US')] <-- this works bc tuples are immutable
        counter += 1

Alternative Way (OOP method):
create classes for each of the tables i.e. astronaut, agency, expedition