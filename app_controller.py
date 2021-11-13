from models.db_model import DB_Model
from models.parser import Parser

def main():
        db = DB_Model()
        parser = Parser(file_name="expeditionData.csv")
        parser.assign_indexes()
        parser.process_file()
        print(parser.__str__())
main()
# if __name__ == main:
#         main()
