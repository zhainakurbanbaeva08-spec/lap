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


w = Warrior(1, "Thor", 100)
m = Mage(2, "Merlin", 80)

attack_event = Event("ATTACK", {"damage": 50})
loot_event = Event("LOOT", {"item": Item(3, "Staff", 40)})

w.handle_event(attack_event)
m.handle_event(loot_event)

print(w.hp)
print(m.inventory)