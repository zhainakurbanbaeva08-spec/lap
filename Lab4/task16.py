class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self.id = player_id
        self.name = name
        self._hp = hp
        self._inventory = []

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)  # hp не может быть отрицательным
    def add_item(self, item):
        self._inventory.append(item)
    def get_inventory(self):
        return self._inventory.copy()

p = Player(1, "Alice", 100)
p.hp -= 20
p.add_item(Item(1, "Sword", 50))
print(p.hp)
print(p.get_inventory())