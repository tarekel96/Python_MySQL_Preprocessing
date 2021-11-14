QUERIES = {
        "INSERT_AGENCY": '''
                        INSERT INTO agency 
                        (agencyID, Name, Origin)
                        VALUES (%s, %s, %s)
                        '''
}

# INSERT_AGENCY = '''INSERT INTO agency 
# (agencyID, Name, Origin)
# VALUES (%s, %s, %s)'''