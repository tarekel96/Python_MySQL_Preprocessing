from os import stat


# helper class for preparing data for db operations
class db_helper():
        
        # given a list of model instances, 
        # create list consisting of tuples of each model's fields 
        @staticmethod
        def get_record_list(models):
                rec_list = []
                for m in models:
                        rec_list.append(m.get_fields())
                return rec_list
        
        @staticmethod
        def is_duplicate(pk, models) -> bool:
                for m in models:
                        if m.id == pk:
                                return True
                return False