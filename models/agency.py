# represents an Agency table of the DB
class Agency():
        def __init__(self, id, name, origin) -> None:
                self.id = id
                self.name = name
                self.origin = origin
        def __str__(self) -> str:
            str_ret = f"Agency\nID: {str(self.id)}"
            str_ret += f"\nName: {self.name}"
            str_ret += f"\nOrigin: {self.origin}\n"
            return str_ret