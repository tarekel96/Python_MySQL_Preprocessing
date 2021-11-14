from models.db_model import DB_Model
from models.parser import Parser
from queries import QUERIES

def main():
        db = DB_Model()
        parser = Parser(file_name="expeditionData.csv")
        parser.process()
        db.assign_table_recs(parser.agencies, "agency")
        # db.bulk_insert(QUERIES['INSERT_AGENCY'], db.records['agency'])
        print(parser.__str__())
        # print("HERE")
        # print(QUERIES['INSERT_AGENCY'])
        # print(db.records['agency'])
        db.bulk_insert(QUERIES['INSERT_AGENCY'], db.records['agency'])
main()
# if __name__ == main:
#         main()
