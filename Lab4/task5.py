class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name
        self.power = power

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        self._items.append(item)

    def get_strong_items(self, min_power: int) -> list[Item]:
        return list(filter(lambda item: item.power >= min_power, self._items))
inv = Inventory()

inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))
inv.add_item(Item(3, "Magic Wand", 80))

strong_items = inv.get_strong_items(40)
print("Сильные предметы:", strong_items)