with open("shop_logs.txt", "w", encoding="utf-8") as f:
    f.write("""2026-02-01;user_1;LOGIN
2026-02-01;user_2;LOGIN
2026-02-01;user_1;BUY;120
2026-02-01;user_3;LOGIN
2026-02-01;user_2;BUY;300
2026-02-01;user_1;BUY;50
2026-02-01;user_2;LOGOUT
""")

unique_users = set()
total_purchases = 0
total_sum = 0
user_spending = {}

with open("shop_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        parts = line.strip().split(";")
        if len(parts) < 3:
            continue

        data = parts[0]
        user_id = parts[1]
        action = parts[2]

        unique_users.add(user_id)

        if action == "BUY" and len(parts) == 4:
            amount = int(parts[3])
            total_purchases = total_purchases + 1
            total_sum = total_sum + amount

            if user_id not in user_spending:
                user_spending[user_id] = amount
            else:
                user_spending[user_id] = user_spending[user_id] + amount

    top_user = max(user_spending, key=user_spending.get) if user_spending else "Нет покупок"
    average_check = total_sum / total_purchases if total_purchases > 0 else 0

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"Уникальных пользователей: {len(unique_users)}\n")
        f.write(f"Всего покупок: {total_purchases}\n")
        f.write(f"Общая сумма: {total_sum}\n")
        f.write(f"Самый активный покупатель: {top_user}\n")
        f.write(f"Средний чек: {average_check:.2f}\n")

    with open("report.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)