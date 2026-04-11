class Inventory:
    def __init__(self):
        self.items={}
    def add_item(self,item):
        self.item[item.id]=item
    def get_item(self):
        return list(self.items.vaules())
class Player:
    def __init__(self, id:int, name:str, hp:int):
        self.id=id
        self.name=name
        self.hp=hp
        self.inventory=Inventory()
    def __str__(self):
        return f"Player(id={self.id}, name='{self.name}', hp={self.hp})"

    @classmethod
    def from_string(cls,data:str):
        try:
            parts=data.split(",")
            if len(parts)!=3:
                raise VauleError("Invalid format")
            id_str, name, hp_str=parts
            id_=int(id_str.strip())
            name_=name.strip().capitalize()
            hp_=int(hp_str.strip())
            return cls(id_,name_,hp_)
        except Exception:
            raise ValueError("Invalid input string")
p = Player.from_string("2, alice , 90")
print(p)