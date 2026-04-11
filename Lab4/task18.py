class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item):
        self._items.append(item)
    def __iter__(self):
        self._index = 0
        return self
    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item
    def strong_items(self, min_power):
        return [item for item in self._items if item.power >= min_power]
inv = Inventory()
inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))

for item in inv:
    print(item)

print(inv.strong_items(40))