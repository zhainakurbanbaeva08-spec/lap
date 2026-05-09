df_group = pd.DataFrame({'user_name': ['John', 'John', 'Alice'], 'order_id': [101, 103, 102], 'total': [1200, 500, 25]})

print("Задача 25 (Sum):\n", df_group.groupby('user_name')['total'].sum())
print("\nЗадача 26 (Mean):\n", df_group.groupby('user_name')['total'].mean())
print("\nЗадача 27 (Count):\n", df_group.groupby('user_name')['order_id'].count())