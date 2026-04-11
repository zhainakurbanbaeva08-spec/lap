class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name
        self.power = power

    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"


class Inventory:
    def __init__(self):
        self._items = {}

    def add_item(self, item: Item):
        self._items[item.id] = item

    def remove_item(self, item_id: int):
        if item_id in self._items:
            del self._items[item_id]

    def get_items(self) -> list[Item]:
        return list(self._items.values())

    def unique_items(self) -> set[Item]:
        return set(self._items.values())

    def to_dict(self) -> dict[int, Item]:
        return self._items.copy()


inv = Inventory()

inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))
inv.add_item(Item(1, "Sword+", 70))
print("Список:", inv.get_items())
print("Уникальные:", inv.unique_items())
print("Словарь:", inv.to_dict())

inv.remove_item(2)
print("После удаления:", inv.get_items())