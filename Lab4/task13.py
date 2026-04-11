from collections import Counter
def analyze_logs(events):
    total_damage = sum(
        e.data.get("damage", 0) for e in events if e.type == "ATTACK"
    )

    damage_by_player = {}
    for e in events:
        if e.type == "ATTACK":
            pid = e.data.get("player_id", 0)
            damage_by_player[pid] = damage_by_player.get(pid, 0) + e.data.get("damage", 0)
    top_player = max(damage_by_player, key=damage_by_player.get, default=None)
    event_counts = Counter(e.type for e in events)
    most_common_event = event_counts.most_common(1)[0][0] if event_counts else None
    return {
        "total_damage": total_damage,
        "top_player": top_player,
        "most_common_event": most_common_event
    }
stats = analyze_logs(events)
print(stats)