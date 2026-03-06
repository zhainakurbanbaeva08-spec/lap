import json

transactions = [
    ["user_id", "amount"],
    ["user_1", 5000],
    ["user_2", 10000],
    ["user_1", 700000],
    ["user_3", 3000],
    ["user_2", 900000],
    ["user_4", 2000]
]

data = transactions[1:]

suspicious_transactions = []
user_operations = {}
suspicious_users = set()
total_suspicious_amount = 0

for row in data:
    user = row[0]
    amount = row[1]

    user_operations[user] = user_operations.get(user, 0) + 1

    if amount>500000:
        suspicious_transactions.append((user, amount))
        suspicious_users.add(user)
        total_suspicious_amount=total_suspicious_amount+amount

for user, count in user_operations.items():
    if count>3:
        suspicious_users.add(user)

with open("fraud_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users)}\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")

with open("fraud_users.json", "w", encoding="utf-8") as f:
    json.dump(list(suspicious_users), f, indent=2)

print("Подозрительные транзакции:", suspicious_transactions)
print("Список подозрительных пользователей:", suspicious_users)
print("Общая сумма подозрительных операций:", total_suspicious_amount)