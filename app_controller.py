from models.db_model import DB_Model
from models.parser import Parser
from queries import QUERIES

def main():
        db = DB_Model()
        parser = Parser(file_name="expeditionData.csv")
        parser.pre_process()
        # insert agency before creating any other table
        db.assign_table_recs(parser.agencies, "agency")
        print(db.records["agency"])
        db.bulk_insert(QUERIES['INSERT_AGENCY'], db.records['agency'])
        # fetch agency IDs and update parser agency list
        agency_ids = db.get_records(QUERIES["GET_AGENCY_ID"])
        parser.assign_agency_ids(agency_ids)
        db.assign_table_recs(parser.agencies, "agency")
        print(db.records["agency"])

        # generates lists of expeditions, astronauts, astro_expeditions
        parser.process()

        # assign expeditions
        db.assign_table_recs(parser.expeditions, "expedition")
        print(db.records['expedition'])
        db.bulk_insert(QUERIES['INSERT_EXPEDITION'], db.records['expedition'])

        # assign astronauts
        db.assign_table_recs(parser.astronauts, "astronaut")
        print(db.records['astronaut'])
        db.bulk_insert(QUERIES['INSERT_ASTRONAUT'], db.records['astronaut'])

        # assign astronaut_expeds
        db.assign_table_recs(parser.astro_expeds, "astro_expedition")
        print(db.records['astro_expedition'])
        db.bulk_insert(QUERIES['INSERT_ASTRO_EXPED'], db.records['astro_expedition'])

main()
# if __name__ == main:
#         main()
