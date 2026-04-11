class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self.id = player_id
        self.name = name
        self.hp = hp
        self.inventory = []

    def handle_event(self, event):
        if event.type == "ATTACK":
            self.hp -= event.data.get("damage", 0)
        elif event.type == "HEAL":
            self.hp += event.data.get("heal", 0)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.inventory.append(item)

class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0) * 0.9
            self.hp -= damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power *= 1.1
        super().handle_event(event)
p = Warrior(1, "Tank", 100)
e = Event("ATTACK", {"damage": 50})

p.handle_event(e)
print(p.hp)