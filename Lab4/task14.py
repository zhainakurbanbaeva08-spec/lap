decide_action = lambda player: (
    "HEAL" if player.hp < 30 else
    "LOOT" if len(player.inventory) < 2 else
    "ATTACK"
)
p = Player(1, "Hero", 20)
print(decide_action(p))