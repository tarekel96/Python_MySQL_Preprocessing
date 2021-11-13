# represents an AstroExpedition table of the DB
class AstroExpedition():
        def __init__(self, id, expedition, astronaut, expedition_id, astronaut_id) -> None:
                self.id = id
                self.expedition = expedition
                self.astronaut = astronaut
                self.expedition_id = expedition_id
                self.astronaut_id = astronaut_id