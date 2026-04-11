class Item:
    def __init__(self, id:int, name:str, power:int):
        self.id=id
        self.name=name.strip()
        self.power=power
    def __hash__(self):
        return hash(self.id)
    def __eq__(self,other):
        return isinstance(other, Item) and self.id==other.id
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"

i = Item(1, " Sword ", 50)
print(i)