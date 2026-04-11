def analyze_inventory(inventories: list) -> dict:
    unique_items = set()
    top_power = None
    for inv in inventories:
        for item in inv._items:
            unique_items.add(item)
            if top_power is None or item.power > top_power.power:
                top_power = item

    return {
        "unique_items": unique_items,
        "top_power": top_power
    }

inv1 = Inventory()
inv1.add_item(Item(1, "Sword", 50))
inv1.add_item(Item(2, "Shield", 30))
inv2 = Inventory()
inv2.add_item(Item(3, "Staff", 70))
inv2.add_item(Item(2, "Shield", 30))
result = analyze_inventory([inv1, inv2])
print(result)