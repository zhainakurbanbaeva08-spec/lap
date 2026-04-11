def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)
events = [
    Event("ATTACK", {"damage": 10}),
    Event("HEAL", {"heal": 5}),
    Event("ATTACK", {"damage": 30})
]

for dmg in damage_stream(events):
    print(dmg)