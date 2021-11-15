# represents an Agency table of the DB
class Astronaut():
        def __init__(self, id, name, age, agency_id) -> None:
                self.id = id
                self.name = name
                self.age = age
                self.agency_id = agency_id
        
        def set_id(self, id):
                self.id = id

        def get_fields(self):
                if self.id == None:
                        return tuple([self.name, self.age, 
                                self.agency_id])
                return tuple([self.id, self.name, self.age, 
                        self.agency_id])

        def __str__(self) -> str:
                str_ret = f"\nAstronaut:\nAstronautID: {str(self.id)}"
                str_ret += f"\nName: {self.name}"
                str_ret += f"\nAge: {self.age}"
                str_ret += f"\nAgencyID: {str(self.agency_id)}\n"
                return str_ret