import pandas as pd

users_data = {'id': [1, 2], 'name': ['John Doe', 'Alice'], 'email': ['john@ex.com', 'alice@ex.com'], 'registration_date': ['2026-03-18', '2026-03-18']}
users_df = pd.DataFrame(users_data)

prods_data = {'id': [1, 2, 3], 'name': ['Laptop', 'Mouse', 'Shirt'], 'category': ['Electronics', 'Electronics', 'Clothing'], 'price': [1200.0, 25.0, 20.0]}
products_df = pd.DataFrame(prods_data)

print("Задача 21 (Users):\n", users_df)
print("Задача 22 (Products):\n", products_df)