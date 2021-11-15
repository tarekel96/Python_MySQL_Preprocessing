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
                        ''',
        "INSERT_ASTRONAUT": '''
                        INSERT INTO astronaut 
                        (astronautID, Name, Age, Agency)
                        VALUES (%s, %s, %s, %s)
                        ''',
        "INSERT_ASTRO_EXPED": '''
                        INSERT INTO astro_expedition 
                        (ID, Expedition, Astronaut)
                        VALUES (%s, %s, %s)
                        '''
}

# INSERT_AGENCY = '''INSERT INTO agency 
# (agencyID, Name, Origin)
# VALUES (%s, %s, %s)'''