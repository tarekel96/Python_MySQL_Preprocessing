from models.db_model import DB_Model
from models.parser import Parser
from queries import QUERIES

def main():
        db = DB_Model()
        parser = Parser(file_name="expeditionData.csv")
        parser.process()
        db.assign_table_recs(parser.agencies, "agency")
        # print(db.records['agency'])
        db.assign_table_recs(parser.expeditions, "expedition")
        # print(db.records['expedition'])
        db.assign_table_recs(parser.astronauts, "astronaut")
        # print(db.records['astronaut'])
        # print(parser.astro_expeds)
        db.assign_table_recs(parser.astro_expeds, "astro_expedition")
        # print(db.records['astro_expedition'])
        
        # print(parser.__str__())
        
        # print("HERE")
        # print(QUERIES['INSERT_AGENCY'])
        # print(db.records['agency'])
        # db.bulk_insert(QUERIES['INSERT_AGENCY'], db.records['agency'])
        # db.bulk_insert(QUERIES['INSERT_EXPEDITION'], db.records['expedition'])
        # db.bulk_insert(QUERIES['INSERT_ASTRONAUT'], db.records['astronaut'])
        db.bulk_insert(QUERIES['INSERT_ASTRO_EXPED'], db.records['astro_expedition'])

main()
# if __name__ == main:
#         main()
