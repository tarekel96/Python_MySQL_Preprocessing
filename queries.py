QUERIES = {
        "INSERT_AGENCY": '''
                        INSERT INTO agency 
                        (agencyID, Name, Origin)
                        VALUES (%s, %s, %s)
                        ''',
        "INSERT_EXPEDITION": '''
                        INSERT INTO expedition 
                        (expeditionNumber, Duration)
                        VALUES (%s, %s)
                        '''
}

# INSERT_AGENCY = '''INSERT INTO agency 
# (agencyID, Name, Origin)
# VALUES (%s, %s, %s)'''