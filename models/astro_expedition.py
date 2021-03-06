# represents an AstroExpedition table of the DB
class AstroExpedition():
        def __init__(self, id, expedition_id, astronaut_id) -> None:
                self.id = id
                # self.expedition = expedition
                # self.astronaut = astronaut
                self.expedition_id = expedition_id
                self.astronaut_id = astronaut_id
        
        def set_id(self, id):
                self.id = id
        
        # do not include the last 2 fields bc they are constraints in the sql table
        def get_fields(self):
                return tuple([self.id, self.expedition_id, self.astronaut_id])
        
        def __str__(self) -> str:
                str_ret = f"\nAstroExp\nAstroExpID: {str(self.id)}"
                # str_ret += f"\nExpedition: {self.expedition}"
                # str_ret += f"\nAstronaut: {self.astronaut}"
                str_ret += f"\nExpID: {self.expedition_id}"
                str_ret += f"\nAstroID: {str(self.astronaut_id)}\n"
                return str_ret