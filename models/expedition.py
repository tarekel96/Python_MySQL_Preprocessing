# represents an Expedition table of the DB
class Expedition():
        def __init__(self, id, duration) -> None:
                self.id = id
                self.duration = duration
        def __str__(self) -> str:
            str_ret = f"\nExpdition:\nExpeditionID: {str(self.id)}"
            str_ret += f"\nDuration: {self.duration}\n"
            return str_ret