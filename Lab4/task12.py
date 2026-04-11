import random
def generate_events(players, items, n):
    events = []
    event_types = ["ATTACK", "HEAL", "LOOT"]

    for player in players:
        for _ in range(n):
            event_type = (lambda: random.choice(event_types))()
            if event_type == "ATTACK":
                data = {"damage": random.randint(5, 50)}
            elif event_type == "HEAL":
                data = {"heal": random.randint(5, 30)}
            else:
                data = {"item": random.choice(items)}
            events.append(Event(event_type, data))
    return events
players = [Player(1, "A", 100), Player(2, "B", 100)]
items = [Item(1, "Sword", 50), Item(2, "Staff", 70)]
events = generate_events(players, items, 3)
print(events)