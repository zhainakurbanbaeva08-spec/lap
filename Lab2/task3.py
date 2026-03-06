data = [
    ["order_id", "user", "items", "total"],
    [1, "Ali", ["phone", "case"], 300000],
    [2, "Dana", ["laptop"], 800000],
    [3, "Ali", ["mouse", "keyboard"], 70000]
]

orders = data[1:]

total_revenue = 0
total_items = 0

max_order = 0
top_user = ""

for order in orders:
    order_id, user, items, total = order

    total_revenue += total

    user_orders[user] = user_orders.get(user, 0) + 1

    if total > max_order:
        max_order = total
        top_user = user

    for item in items:
        total_items += 1
        item_count[item] = item_count.get(item, 0) + 1

most_popular_item = max(item_count, key=item_count.get)

summary = {
    "total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": most_popular_item,
    "total_orders": len(orders)
}

print("Total revenue:", total_revenue)
print("Most popular item:", most_popular_item)
print("Top user:", top_user)
print("Summary:", summary)